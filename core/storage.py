import os
import pickle
from typing import List, Dict, Any

# File paths for the binary database
USERS_FILE = "users.bin"
BOOKS_FILE = "books.bin"
LOANS_FILE = (
    "loans.bin"  # Agrego esta también porque vi manage_loans_menu en tu traceback
)


def save_data(filepath: str, data: Any) -> None:
    """
    Overwrites the binary file with the current dictionary/list.
    """
    # Using 'wb' (Write Binary) mode to serialize the Python object
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def load_data(filepath: str, default_data: Any = None) -> Any:
    """
    Reads the binary file and reconstructs it back into Python objects.
    Returns the default_data if the file doesn't exist or is empty.
    """
    if default_data is None:
        default_data = []  # Could be [] or {} depending on the base structure

    # If the file does not exist, create it with the default structure
    if not os.path.exists(filepath):
        save_data(filepath, default_data)
        return default_data

    try:
        # Using 'rb' (Read Binary) mode to deserialize the data
        with open(filepath, "rb") as file:
            return pickle.load(file)
    except EOFError:
        # Handle the exception in case the binary file was created but is completely empty
        return default_data
