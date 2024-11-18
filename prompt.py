class Prompt:
    @staticmethod
    def create_prompt(text, example):
        """
        Creates a prompt for extracting structured data from text.

        Args:
            text: The input text.

        Returns:
            The prompt string.
        """
        system_prompt = """As a seasoned Analyst with over a decade of experience, you possess an exceptional eye for detail and a profound ability to understand and extract complex information."""
        prompt = (
            f"Based on the given context: {text},"
            f"""
              - Extract all structured data from the provided text.
              - Identify all table-like structures within the text.
              - Extract the relevant tables and provide a JSON output.
              - Group tables with similar fields into the same JSON object.
              - Use logical key-value structures to organize the data.
              - Do not alter any data or use your own thoughts in the data manipulation.
              - Ensure the data is only from the text given and not generated on your own.
              - In cases where multi-indexing is used, convert it into a simple form by merging the column names, but maintain the same structure without pivoting or transposing it.
              - Ensure the JSON output is properly formatted with appropriate keys and values.
              - Correctly identify the column names, rows, and all the data.
              - Structure the JSON output in the most similar way possible to the structure of the data in the Input text.
              - Preserve the integrity and accuracy of the data during extraction.
              - Handle any special characters or formatting issues in the text appropriately.
              - The end goal is to have the structured data in the form of an Excel file.

              **Example:**

              {example}

              **Instructions for JSON Output:**

              - The JSON output should include a "table_name" key, which represents the name of the table.
              - The "columns" key should contain a list of column names.
              - The "data" key should contain a list of lists, where each inner list represents a row in the table.

              **Additional Notes:**

              - The JSON output should be structured in a way that allows for easy conversion to an Excel file.
              - The table name should be extracted from the text, if possible.
              - The column names should be extracted from the text, if possible.
              - The data should be extracted from the text, if possible.
              - The JSON output should be properly formatted and indented.
              """
        )
        return prompt, system_prompt
    
    def create_json_csv_prompt(response):
        return f"""
    Please convert the following JSON data into a CSV format:

    Input JSON: {response}

    Requirements:
    1. Correctly identify and handle multi-indexing if present in the JSON format.
    2. Ensure the CSV structure retains all data without any loss.
    3. Merge column names if necessary to resolve multi-indexing issues.
    4. Use best practices to structure the CSV for the most accurate results.
    5. Return only the CSV content without any additional text (no headers or footers).
    6. Use semicolons as separators to prevent issues with numbers that contain commas.
    7. Create different CSVs for different JSON keys if the JSON contains multiple keys. Identify and correctly create separate CSVs for each key.
    8. Ensure the CSV files are named appropriately based on the JSON keys to avoid any confusion.
    9. Add a partition line (e.g., "-----") between different CSV files in the response to clearly separate them.
    10. Correctly identify and include all field names in the CSV files.
    11. If the json has tables name key provide its value as the first row of the data frame and keep the rest of the values empty for it, the table name would then be used as the file name for the csv.
    Thank you.
    """
    def image_to_text_prompt():
        return """
        - As an expert in data extraction, your task is to accurately identify and extract table structures from the provided image.
        - Focus solely on outputting the structured JSON representation of the tables, without any additional commentary.
        - The image may contain multiple tables; ensure each is extracted distinctly.
        - Pay close attention to accurately capturing column names, and if a column lacks a name, label it as 'Category'.
        - Ensure the JSON structure is precise for conversion into data frames.
        - Retain all symbols such as '+', '-', '(', ')', etc., exactly as they appear in the image.
        - Avoid any assumptions or additions beyond the visible data.
        """