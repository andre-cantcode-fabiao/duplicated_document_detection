import os

from app.storage.local_storage import LocalStorageHandler
from app.storage import StorageHandler

STORAGE_SERVICE = os.environ.get('STORAGE_SERVICE')

# Dependency injection to select the storage handler
def get_storage_handler() -> StorageHandler:

    if STORAGE_SERVICE == 'local':
        return LocalStorageHandler()
    else:
        raise ValueError(F"Storage service {STORAGE_SERVICE} not supported")
