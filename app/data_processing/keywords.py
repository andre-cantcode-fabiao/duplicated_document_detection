from app.prompting.chatgpt import chat_gpt
from ast import literal_eval
import json
import os
import logging
from dotenv import load_dotenv

load_dotenv()

# NOTE In a large scale application we would use a database to store the keywords

KEYWORDS_FILE_PATH = os.environ.get("KEYWORDS_FILE_PATH")

def ensure_keywords_file_exists():
    if not os.path.exists(KEYWORDS_FILE_PATH):
        with open(KEYWORDS_FILE_PATH, 'w') as file:
            json.dump({}, file)

ensure_keywords_file_exists()

def read_keywords_from_json() -> dict:
    # Read the keywords from a JSON file
    with open(KEYWORDS_FILE_PATH, "r") as file:
        keywords = json.load(file)
    return keywords

def save_keywords_to_json(keywords):
    # Save the extracted keywords to a JSON file
    with open(KEYWORDS_FILE_PATH, "w") as file:
        json.dump(keywords, file)

def extract_keywords(text: str) -> list:

    # Use the GPT-3 model to extract keywords from the text
    prompt = f"""Extract the 10 most relevant keywords from the following text: {text}\n
    The keywords should be extracted from the text and should be relevant to the content.\n
    The keywords should be single words.\n
    The keywords should be in lowercase.\n\n
    Output the keywords as a list of strings in Python format:\n
    ['keyword1', 'keyword2', 'keyword3', ...]
    """

    response = chat_gpt(prompt)

    try:
        # Convert the response to a list of keywords
        keywords = literal_eval(response)
    except Exception as e:
        logging.error(f"An error occurred while extracting keywords: {e}")
        raise ValueError("Error extracting keywords from the text.")

    return keywords

def save_new_keywords_to_json(filename: str, keywords: list):

    keywords_dict = read_keywords_from_json()
    if filename in keywords_dict:
        logging.warning(f"Keywords for {filename} already exist in the JSON file.")
    keywords_dict[filename] = keywords
    save_keywords_to_json(keywords_dict)


def find_matching_keys(new_list, threshold=5):

    keywords = read_keywords_from_json()
    logging.debug(f"Keywords from JSON: {keywords}")
    matching_keys = []

    for key, string_list in keywords.items():
        match_count = sum(1 for string in new_list if string in string_list)

        if match_count > threshold:
            matching_keys.append(key)

    return matching_keys
