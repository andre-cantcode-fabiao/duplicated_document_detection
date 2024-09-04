
# Duplicated Document Detection Service

This service helps to detect duplicate documents by analyzing the content of uploaded files.

## Prerequisites

Before you start, ensure you have the following installed:

- Docker
- Docker Compose

## Getting Started
### Setting Up ChatGPT

Change the OPENAI_API_KEY to your personal que in the '.env' file.

'''bash
OPENAI_API_KEY=your_openai_api_key
'''

### Running the Service Locally

To start the service locally, use Docker Compose:

```bash
docker-compose up --build
```

This command builds and starts the service on your local machine.

### Testing the Service

You can test the service by uploading a document using `curl` or a batch file (for Windows users).

#### Using `curl`

Run the following command, replacing `filename.docx` with the name of your document and the path with the location of your file:

```bash
curl -X POST "http://localhost:8000/upload/?filename=filename.docx" -F "file=@/path/to/your/file.docx"
```

#### Using the Batch File (Windows Users)

For Windows users, you can test the service with the provided batch file:

```bash
upload_test.bat
```
