"""
Snippet Manager

A lightweight local snippet storage utility.

Provides functions to manage snippets with author handles.

Author: Yashvi
"""

import json
import os
import uuid


# File name where local snippets are saved
STORAGE_FILE = os.path.join(
    os.path.dirname(__file__),
    "snippets.json"
)


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


def add_snippet(title, code, author="Anonymous"):
    """Create a new snippet with a unique ID and author handle."""
    snippets = load_snippets()

    snippet_id = str(uuid.uuid4())[:8]

    snippets[snippet_id] = {
        "id": snippet_id,
        "title": title,
        "code": code,
        "author": author
    }

    save_snippets(snippets)

    return snippet_id


def list_snippets(author_filter=None):
    """Fetch stored snippets, optionally filtered by author."""
    snippets = load_snippets()

    if author_filter:
        return {
            snippet_id: data
            for snippet_id, data in snippets.items()
            if data.get("author", "").lower() == author_filter.lower()
        }

    return snippets


def get_snippet(snippet_id):
    """Get a single snippet using its unique ID."""
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
