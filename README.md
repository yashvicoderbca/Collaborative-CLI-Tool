# Collaborative CLI Tool

A lightweight, network-based command-line snippet manager powered by a FastAPI REST backend and local persistent JSON storage.

## Status

- **Core Engine:** Functional (Part 1)
- **Networking & REST API:** Complete (Part 2)
- **Multi-user Handles and Filtering:** Complete (Part 3)
- **Keyword Search & Clipboard Support:** Complete (Part 4)

## Overview

Collaborative CLI Tool allows developers to store, retrieve, search, filter, copy, and delete code snippets directly from their terminal.

It uses a client-server architecture where the CLI communicates with a FastAPI server through HTTP requests.

## Features

- **Add snippets:** Create code snippets with custom titles, code content, and author handles using `--author`.
- **List snippets:** View all stored snippets.
- **Filter snippets:** Filter snippets by author handle.
- **Search by title:** Search snippets using keywords contained in the title.
- **Search by code:** Search snippets using keywords contained in the code.
- **Combined search:** Search by title, code, and author together.
- **View snippet:** Fetch complete snippet details using unique short IDs.
- **Copy snippet code:** Copy the code of a snippet directly to the system clipboard using `--copy`.
- **Delete snippets:** Remove outdated or unwanted snippets by ID.
- **Persistent storage:** Store snippets locally in a JSON file.
- **Robust exception handling:** Handle network connection failures and HTTP errors.

## Tech Stack

- **Programming Language:** Python 3.x
- **API Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **HTTP Client:** Requests
- **Data Model Validation:** Pydantic
- **Clipboard Support:** Pyperclip
- **Storage:** Local JSON file

## Project Structure

```text
Collaborative-CLI-Tool/
│
├── cli.py
├── server.py
├── snippet_manager.py
├── requirements.txt
├── README.md
├── .gitignore
└── snippets.json

