import PyPDF2
import os
from PIL import Image
import io

class PDFTools:
    
    @staticmethod
    def open_pdf(pdf_path):
        pdf_document = open(pdf_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_document)
        return pdf_document, pdf_reader

    @staticmethod
    def close_pdf(pdf_document):
        if pdf_document:
            pdf_document.close()

    @staticmethod
    def extract_images(pdf_path, output_folder):
        """
        Extracts images from the PDF file and saves them to the specified output folder in PNG format.

        :param pdf_path: Path to the PDF file.
        :param output_folder: Folder where the extracted images will be saved.
        """
        pdf_document, pdf_reader = PDFTools.open_pdf(pdf_path)
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        image_bytes = xObject[obj]._data
                        image_filename = f"{output_folder}/image_page{page_number+1}_{obj[1:]}.png"
                        
                        temp_image = io.BytesIO(image_bytes)
                        try:
                            image = Image.open(temp_image)
                            image.verify()
                            with open(image_filename, "wb") as image_file:
                                image_file.write(image_bytes)
                        except (IOError, SyntaxError) as e:
                            print(f"Skipping invalid image on page {page_number+1}, object {obj[1:]}: {e}")
        PDFTools.close_pdf(pdf_document)
        print(f"Images extracted and saved to {output_folder}")

    @staticmethod
    def read_text(pdf_path):
        """
        Reads the PDF file and writes each page's text content to a separate text file
        in a folder named after the PDF file. Returns the folder name.
        """
        try:
            folder_name = os.path.splitext(os.path.basename(pdf_path))[0]
            os.makedirs(folder_name, exist_ok=True)
            
            pdf_document, pdf_reader = PDFTools.open_pdf(pdf_path)
            for i, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                with open(os.path.join(folder_name, f'page_{i+1}.txt'), 'w', encoding='utf-8') as text_file:
                    text_file.write(page_text)
            PDFTools.close_pdf(pdf_document)
            return folder_name
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
            return None