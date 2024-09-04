import os
import logging
from fastapi import UploadFile, HTTPException
from app.storage import StorageHandler
from app.data_processing.docx import extract_text_from_docx, extract_text_from_docx_path
from app.data_processing import file_similarity
from app.data_processing import keywords

STORAGE_FOLDER_PATH = os.environ.get('STORAGE_FOLDER_PATH')

# Local storage handler implementation
class LocalStorageHandler(StorageHandler):
    def __init__(self, base_path: str = STORAGE_FOLDER_PATH):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    async def save_file(self, file: UploadFile, filename: str) -> str:
        file_path = os.path.join(self.base_path, filename)
        try:

            file_content = await file.read()
            await file.seek(0)

            with open(file_path, "wb") as f:
                f.write(file_content)

            logging.info(f"File saved locally: {file_path}")
            return file_path
        except Exception as e:
            logging.error(f"Failed to save file locally: {e}")
            raise HTTPException(status_code=500, detail="Failed to save file locally.") from None

    async def file_exists(self, file: UploadFile, filename: str) -> bool:

        logging.debug(f"Checking if file already exists")
        file_content = await file.read()
        await file.seek(0)
        logging.debug(f"File content read: {file_content[:100]}")

        text_data = extract_text_from_docx(file_content)
        logging.debug(f"Extracted text data: {text_data[:100]}")

        keywords_list = keywords.extract_keywords(text_data)
        logging.debug(f"Extracted keywords: {keywords_list}")

        potential_matches = keywords.find_matching_keys(keywords_list)
        logging.debug(f"Potential matches: {potential_matches}")

        for match in potential_matches:
            logging.debug(f"Comparing with potential match: {match}")
            file_to_compare = os.path.join(self.base_path, match)
            text_data_to_compare = extract_text_from_docx_path(file_to_compare)
            similarity = file_similarity.compare_text_data(text_data, text_data_to_compare)

            logging.info(f"Similarity between {filename} and {match}: {similarity}")

            if similarity > 90:
                return True

        keywords.save_new_keywords_to_json(filename, keywords_list)

        return False