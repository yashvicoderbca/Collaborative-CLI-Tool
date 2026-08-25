"""
Collaborative CLI Tool - FastAPI Server

Provides REST API endpoints supporting user handles
and author filtering.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from snippet_manager import (
    add_snippet,
    list_snippets,
    get_snippet,
    delete_snippet,
)

# Initialize FastAPI application
app = FastAPI(
    title="Collaborative CLI Tool - API Server"
)


# Data model for incoming snippet request
class SnippetCreate(BaseModel):
    title: str
    code: str
    author: Optional[str] = "Anonymous"


# Health check endpoint
@app.get("/")
def read_root():
    """Health check endpoint."""
    return {
        "message": "Collaborative CLI Tool API is running!"
    }


# Create a new snippet
@app.post("/snippets")
def create_snippet(snippet: SnippetCreate):
    """API endpoint to create a snippet with an author."""
    snippet_id = add_snippet(
        snippet.title,
        snippet.code,
        snippet.author
    )

    return {
        "status": "success",
        "id": snippet_id,
        "message": "Snippet created successfully"
    }


# List all snippets
@app.get("/snippets")
def fetch_all_snippets(author: Optional[str] = None):
    """API endpoint to retrieve snippets, optionally filtered by author."""
    snippets = list_snippets(author_filter=author)

    return {
        "status": "success",
        "data": snippets
    }


# Get a snippet by ID
@app.get("/snippets/{snippet_id}")
def fetch_snippet(snippet_id: str):
    """API endpoint to retrieve a single snippet by ID."""
    snippet = get_snippet(snippet_id)

    if not snippet:
        raise HTTPException(
            status_code=404,
            detail=f"Snippet with ID '{snippet_id}' not found"
        )

    return {
        "status": "success",
        "data": snippet
    }


# Delete a snippet by ID
@app.delete("/snippets/{snippet_id}")
def remove_snippet(snippet_id: str):
    """API endpoint to delete a snippet by ID."""
    deleted = delete_snippet(snippet_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Snippet with ID '{snippet_id}' not found"
        )

    return {
        "status": "success",
        "message": f"Snippet '{snippet_id}' deleted successfully"
    }


# Run server directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
