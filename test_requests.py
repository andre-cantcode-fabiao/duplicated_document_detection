import requests

# Define the URL of the FastAPI upload endpoint
url = "http://localhost:8000/upload/"

# Define the path to the .docx file you want to upload
file_path = "d4.docx"  # Replace with the path to your .docx file

# Define the filename you want to store the file as
filename = "uploaded_test_file_2.docx"

# Open the file in binary mode
with open(file_path, "rb") as file:
    # Prepare the files dictionary to send in the request
    files = {
        "file": (file_path, file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    }

    # Send the POST request to upload the file with the filename as a query parameter
    response = requests.post(url, files=files, params={"filename": filename})

# Print the response from the server
print(response.status_code)
print(response.json())