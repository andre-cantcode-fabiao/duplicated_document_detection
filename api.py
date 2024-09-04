from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
from app.storage.storage_handler import StorageHandler, get_storage_handler
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create a folder named 'documents' if it doesn't exist
STORAGE_FOLDER_PATH = os.environ.get('STORAGE_FOLDER_PATH')
os.makedirs(STORAGE_FOLDER_PATH, exist_ok=True)

app = FastAPI()

@app.post("/upload/")
async def upload_file(
    filename: str,
    file: UploadFile = File(...),
    handler: StorageHandler = Depends(get_storage_handler)
):
    # Check if the uploaded file is a .docx file
    if not filename.endswith(".docx") or not file.filename.endswith(".docx"):
        raise HTTPException(status_code=400, detail="Only .docx files are allowed.")

    # Check if the file already exists based on content
    if await handler.file_exists(file, filename):
        raise HTTPException(status_code=418, detail="A file with the same content already exists.")

    # Save the uploaded file using the storage handler
    try:
        file_path = await handler.save_file(file, filename)
    except HTTPException as e:
        raise e

    return JSONResponse(content={"message": f"File '{filename}' uploaded successfully to {file_path}."})

@app.get("/files/")
async def list_files():
    # List all files in the STORAGE_FOLDER_PATH directory
    try:
        files = os.listdir(STORAGE_FOLDER_PATH)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to list files.")

    return JSONResponse(content={"files": files})
