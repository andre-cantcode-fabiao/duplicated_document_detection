from fastapi import UploadFile
from abc import ABC, abstractmethod

# Define a storage handler protocol for different backends
class StorageHandler(ABC):
    @abstractmethod
    def save_file(self, filename: str, file: UploadFile) -> str:
        pass

    @abstractmethod
    def file_exists(self, file: UploadFile, filename: str) -> bool:
        pass