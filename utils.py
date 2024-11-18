import logging
import os
import yaml
import pandas as pd
from openai import OpenAI
import base64

class Utility:
    def __init__(self, creds_file='creds.yaml'):
        self.api_key, self.model_name = self._get_api_and_model_from_creds(creds_file)

    @staticmethod
    def _get_api_and_model_from_creds(creds_file='creds.yaml'):
        """
        Loads API key and model name from creds.yaml.

        :return: A tuple containing the API key and model name.
        """
        with open(creds_file, 'r') as file:
            creds = yaml.safe_load(file)

        model_name = creds['openai']['openai_model']
       # api_key = creds['openai']['openai_key']

        return model_name

    @staticmethod
    def get_openai_response(api_key, model_name, prompt, system_prompt):
        """
        Sends a prompt to the OpenAI API and retrieves the response.

        :param api_key: The API key for OpenAI.
        :param model_name: The model name to use for the request.
        :param prompt: The user prompt to send to the model.
        :param system_prompt: The system prompt to set the context for the model.
        :return: The content of the response from the OpenAI model.
        """
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        response_content = completion.choices[0].message.content
        # Log the OpenAI response
        logging.info(f"Prompt: {prompt}\nOpenAI Response: {response_content}")
        return response_content

    @staticmethod
    def create_excel_from_csvs(folder_path):
        """
        Creates an Excel file from CSV files in a specified folder.

        :param folder_path: Path to the folder containing CSV files.
        """
        csv_files = sorted(
            [f for f in os.listdir(folder_path) if f.endswith('.csv')],
            key=lambda x: int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else float('inf')
        )

        output_file = f"{folder_path}.xlsx"
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            for csv_file in csv_files:
                try:
                    df = pd.read_csv(os.path.join(folder_path, csv_file))
                    sheet_name = csv_file.split('.')[0]
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                except Exception as e:
                    print(f"Error processing file {csv_file}: {e}")

        print(f"Excel file '{output_file}' with multiple sheets has been created successfully.")

    @staticmethod
    def extract_text_from_image(api_key, img, prompt):
        """
        Extracts text from an image using OpenAI Vision API.

        :param api_key: The API key for OpenAI.
        :param img: The image to extract text from.
        :param prompt: The prompt to guide the extraction.
        :return: The extracted text.
        """
        # Load the image
        with open(img, "rb") as image_file:
            image_bytes = image_file.read()
        
        # Encode the image
        base64_image = base64.b64encode(image_bytes).decode('utf-8')

        # Use OpenAI Chat API to extract text
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )

        # Extract the text from the response
        text = response.choices[0].message.content

        return text