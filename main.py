import os
import shutil
import pandas as pd
from io import StringIO
import streamlit as st
from prompt import Prompt
from utils import Utility
from folders import PDFTools
from table_detector import TableDetector
from examples import Example
import csv
import logging

logging.basicConfig(level=logging.INFO)

def extract_images(input_pdf):
    """
    Extracts images from a PDF file and saves them to a designated output folder.

    Parameters:
    - input_pdf (str): The path to the PDF file from which images are to be extracted.

    Returns:
    - str: The path to the folder where the extracted images are saved.
    """
    output_folder = f"{os.path.splitext(input_pdf)[0]}_images"
    os.makedirs(output_folder, exist_ok=True)
    logging.info(f"Extracting images from {input_pdf} to {output_folder}")
    PDFTools.extract_images(pdf_path=input_pdf, output_folder=output_folder)
    logging.info(f"Image extraction complete.")
    return output_folder

def filter_images(output_folder):
    """
    Filters images in a folder, removing those that do not contain tabular data.

    Parameters:
    - output_folder (str): The path to the folder containing images to be filtered.

    Returns:
    - list: A list of image filenames that contain tabular data.
    """
    logging.info(f"Filtering images in {output_folder}")
    images = [f for f in os.listdir(output_folder) if f.endswith('.png')]
    for image in images:
        image_path = os.path.join(output_folder, image)
        if not TableDetector.detect_tabular_data(image_path):
            os.remove(image_path)
            logging.info(f"Removed non-tabular image: {image}")
    logging.info(f"Image filtering complete.")
    return images

def extract_text_from_images(images, output_folder, api_key, img_prompt):
    """
    Extracts text from images using an API and saves the text to files.

    Parameters:
    - images (list): A list of image filenames to process.
    - output_folder (str): The path to the folder where text files will be saved.
    - api_key (str): The API key for accessing the text extraction service.
    - img_prompt (str): The prompt to guide the text extraction process.
    """
    logging.info(f"Extracting text from images in {output_folder}")
    for image in images:
        image_path = os.path.join(output_folder, image)
        if os.path.exists(image_path):
            page_number = image.split('_')[1].replace('page', '')
            img_res = Utility.extract_text_from_image(api_key=api_key, prompt=img_prompt, img=image_path)
            text_file_path = os.path.join(output_folder, f"page_{page_number}.txt")
            with open(text_file_path, 'w') as text_file:
                text_file.write(img_res)
            os.remove(image_path)
            logging.info(f"Extracted text from {image} and saved to {text_file_path}")
    logging.info(f"Text extraction complete.")


def move_files(output_folder, folder_name):
    """
    Moves files from one folder to another.

    Parameters:
    - output_folder (str): The path to the source folder containing files to move.
    - folder_name (str): The path to the destination folder where files will be moved.
    """
    logging.info(f"Moving files from {output_folder} to {folder_name}")
    for file_name in os.listdir(output_folder):
        source_file = os.path.join(output_folder, file_name)
        destination_file = os.path.join(folder_name, file_name)
        if os.path.isfile(source_file):
            shutil.move(source_file, destination_file)
            logging.info(f"Moved file: {file_name}")
    logging.info(f"File move complete.")

def process_text_files(input_folder, output_folder, model_name, api_key):
    """
    Processes text files to extract structured data and convert it to CSV format.

    Parameters:
    - input_folder (str): The path to the folder containing text files to process.
    - output_folder (str): The path to the folder where CSV files will be saved.
    - model_name (str): The name of the model to use for data extraction.
    - api_key (str): The API key for accessing the data extraction service.
    """
    logging.info(f"Processing text files in {input_folder}")
    example = Example.get_examples()
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            with open(os.path.join(input_folder, filename), 'r') as file:
                pdf_text = file.read()
            prompt, system_prompt = Prompt.create_prompt(pdf_text, example)
            try:
                response = Utility.get_openai_response(prompt=prompt, system_prompt=system_prompt, model_name=model_name, api_key=api_key)
                response = response.replace("```json", "").replace("```", "")
                json_csv_prompt = Prompt.create_json_csv_prompt(response)
                res = Utility.get_openai_response(prompt=json_csv_prompt, system_prompt=system_prompt, model_name=model_name, api_key=api_key)
                logging.info(f"First file response: {res}")
                res = res.replace("```csv", "").replace("```", "")
                
                csv_filename = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.csv')
                with open(csv_filename, 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    for line in res.strip().split('\n'):
                        csvwriter.writerow(line.split(';'))
                logging.info(f"Converted {filename} to CSV and appended to {output_folder}")
            except Exception as e:
                logging.error(f"Error processing {filename}: {e}")
                
    logging.info(f"Text file processing complete.")

def read_csvs_from_folder(folder_name):
    """
    Reads CSV files from a folder and returns them as a dictionary of DataFrames.

    Parameters:
    - folder_name (str): The path to the folder containing CSV files.

    Returns:
    - dict: A dictionary where keys are filenames and values are DataFrames.
    """
    logging.info(f"Reading CSV files from {folder_name}")
    csv_files = [os.path.join(folder_name, file) for file in os.listdir(folder_name) if file.endswith('.csv')]
    dataframes = {}
    for csv_file in csv_files:
        with open(csv_file, 'r') as file:
            content = file.read()
            split_contents = content.split('-----')
            for i, split_content in enumerate(split_contents):
                try:
                    df = pd.read_csv(StringIO(split_content))
                    if not df.empty:
                        dataframes[f"{os.path.basename(csv_file).split('.')[0]}_{i+1}"] = df
                except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
                    st.warning(f"Warning: Skipping file {csv_file} part {i+1} due to error: {e}")
                    continue
    logging.info(f"CSV file reading complete.")
    return dataframes

def create_final_dataframe(dataframes):
    """
    Combines multiple DataFrames into a single DataFrame with additional metadata.

    Parameters:
    - dataframes (dict): A dictionary of DataFrames to combine.

    Returns:
    - DataFrame: A combined DataFrame with metadata columns.
    """
    logging.info("Creating final DataFrame")
    max_columns = max(df.shape[1] for df in dataframes.values())
    final_table = []
    for page, df in dataframes.items():
        page_no, table_no = page.rsplit('_', 1)
        page_no = str(page_no)
        table_no = str(table_no)
        column_no = df.shape[1]
        header_row = [page_no, table_no, 'T.header', str(column_no)] + df.columns.tolist() + ['null'] * (max_columns - len(df.columns))
        final_table.append(header_row)
        for index, row in df.iterrows():
            row_as_str = [str(item) for item in row.tolist()]
            value_row = [page_no, table_no, f'T.value', str(column_no)]
            value_row.extend(row_as_str)
            value_row += ['null'] * (max_columns - len(row_as_str))
            final_table.append(value_row)
    final_df = pd.DataFrame(final_table, columns=['page_no', 'table_no', 'type', 'column_no'] + [f'col{i+1}' for i in range(max_columns)])
    logging.info("Final DataFrame created")
    return final_df

def save_final_dataframe(final_df, folder_name):
    """
    Saves the final DataFrame to a CSV file.

    Parameters:
    - final_df (DataFrame): The DataFrame to save.
    - folder_name (str): The path to the folder where the CSV file will be saved.

    Returns:
    - str: The path to the saved CSV file.
    """
    logging.info(f"Saving final DataFrame to {folder_name}")
    csv_file_path = os.path.join(folder_name, 'final_output.csv')
    os.makedirs(folder_name, exist_ok=True)
    final_df.to_csv(csv_file_path, index=False, sep=';')
    logging.info(f"Final DataFrame saved to {csv_file_path}")
    return csv_file_path

def main():
    """
    Main function to execute the PDF processing workflow using Streamlit.
    """
    st.title("PDF to CSV Converter")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    api_key = st.text_input("Enter your OpenAI API key", type="password") # Added API key input
    
    if uploaded_file is not None and api_key is not None:
        input_pdf = uploaded_file.name
        with open(input_pdf, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Start Processing"):
            with st.empty():
                progress_bar = st.progress(0)
                log_placeholder = st.empty()
                
                logs = []
                
                def log_update(message):
                    logs.append(message)
                    log_placeholder.text('\n'.join(logs))

                log_update("Starting process...")
                
                try:
                    progress_bar.progress(10)
                    # Extract images from PDF
                    images_folder = extract_images(input_pdf)
                    log_update(f"Images extracted to {images_folder}")
                    progress_bar.progress(20)
                    # Filter images, keeping only those with tables
                   # images = filter_images(images_folder)
                   # log_update(f"Images filtered. {len(images)} images remain.")
                    progress_bar.progress(30)
                    model_name = Utility._get_api_and_model_from_creds() #Removed this line
                    #model_name = "gpt-3.5-turbo" #Added default model name
                    img_prompt = Prompt.image_to_text_prompt()
                    # Extract text from images
                    extract_text_from_images(images, images_folder, api_key, img_prompt)
                    log_update("Text extracted from images.")
                    progress_bar.progress(40)
                    # Create a folder for extracted text and move files there
                    text_folder = PDFTools.read_text(pdf_path=input_pdf)
                    move_files(images_folder, text_folder)
                    log_update(f"Files moved to {text_folder}")
                    progress_bar.progress(50)
                    # Process text files to create CSVs
                    process_text_files(input_folder=text_folder, output_folder=images_folder, model_name=model_name, api_key=api_key)
                    log_update("Text files processed.")
                    progress_bar.progress(60)
                    # Read CSVs into dataframes
                    dataframes = read_csvs_from_folder(images_folder)
                    log_update("CSV files read.")
                    progress_bar.progress(70)
                    # Create final dataframe
                    final_df = create_final_dataframe(dataframes)
                    log_update("Final DataFrame created.")
                    progress_bar.progress(80)
                    log_placeholder.empty()
                    st.write("Final DataFrame:")
                    st.dataframe(final_df)
                    progress_bar.progress(90)
                    # Save final dataframe
                    csv_file_path = save_final_dataframe(final_df, text_folder)
                    log_update(f"Final DataFrame saved to {csv_file_path}")
                    progress_bar.progress(100)
                    st.success(f"Final DataFrame has been saved to {csv_file_path}")
                    st.download_button(label="Download CSV", data=open(csv_file_path, 'rb').read(), file_name='final_output.csv', mime='text/csv')
                except Exception as e:
                    log_update(f"An error occurred: {e}")
                    st.error(f"An error occurred during processing: {e}")


if __name__ == "__main__":
    main()