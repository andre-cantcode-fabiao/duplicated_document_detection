import os
from app.storage.local_storage import LocalStorageHandler
import logging

# Set the logging level to INFO
# logging.basicConfig(level=logging.INFO)

# Directory containing the test files
test_data_dir = "test_data"

# Initialize the storage handler
storage = LocalStorageHandler()

filenames = ['test_data/documents/lisbon_earthquake_with_lorem_ipsum.docx']

# Iterate over all files in the test_data directory
for filename in os.listdir(test_data_dir):
    file_path = os.path.join(test_data_dir, filename)

    # Open each file in binary mode
    with open(file_path, "rb") as file:
        print(f"Processing file: {filename}")

        if not storage.file_exists(file, filename):
            print(f'storaage file {filename} does not exist')
            storage.save_file(file, filename)
            print(f'file {filename} saved')
        else:
            print(f'file {filename} already exists')

        print("\n\n")