import os
import json
from typing import List, Dict, Any

# Dynamically resolve the absolute path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Define the text file paths
BOOKS_FILE = os.path.join(DATA_DIR, "books.txt")
USERS_FILE = os.path.join(DATA_DIR, "users.txt")


def save_data(filepath: str, data: List[Dict[str, Any]]) -> None:
    """Writes a list of dictionaries to a JSON-formatted text file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_data(filepath: str) -> List[Dict[str, Any]]:
    """Loads a JSON-formatted text file into a list of dictionaries."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
