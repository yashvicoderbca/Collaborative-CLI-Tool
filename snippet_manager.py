"""
Snippet Manager
===============

A lightweight local snippet storage utility.

This module provides functionality to:
- Add new code snippets
- List all stored snippets
- Retrieve a snippet by ID
- Delete snippets
- Persist snippet data in a local JSON file

Storage:
    snippets.json

Author:
    Yashvi


"""
import json
import os
import uuid


# Storage File Path Configuration
STORAGE_FILE = os.path.join(os.path.dirname(__file__), "snippets.json")


def load_snippets():
    """Load all snippets from the local JSON file safely."""
    if not os.path.exists(STORAGE_FILE):
        return {}

    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_snippets(snippets):
    """Save the snippets dictionary to the local JSON file."""
    with open(STORAGE_FILE, "w", encoding="utf-8") as file:
        json.dump(snippets, file, indent=4)


def add_snippet(title, code):
    """Create a new snippet with a unique short ID."""
    snippets = load_snippets()

    snippet_id = str(uuid.uuid4())[:8]

    snippets[snippet_id] = {
        "id": snippet_id,
        "title": title,
        "code": code
    }

    save_snippets(snippets)

    return snippet_id


def list_snippets():
    """Fetch all the stored snippets."""
    return load_snippets()


def get_snippet(snippet_id):
    """Retrieve a specific snippet by its unique ID."""
    snippets = load_snippets()

    return snippets.get(snippet_id)


def delete_snippet(snippet_id):
    """Delete a snippet using its unique ID."""
    snippets = load_snippets()

    if snippet_id in snippets:
        del snippets[snippet_id]
        save_snippets(snippets)
        return True

    return False
