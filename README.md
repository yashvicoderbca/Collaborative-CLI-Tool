# 🚀 Collaborative CLI Tool
A lightweight, network command-line snippet manager powered by a FastAPI REST backend and local persistent JSON storage. 

## Status
-**Core Engine:** Functional(part 1)
-**networking & REST API:** Complete(part2)
-**multi-user handles and filtering:** complete(part 3)

## Overview
Collaborative CLI Tool allows developers to store, retrieve, filter, and delete code snippets directly from their terminal. It uses a client-server architecture where the CLI communicates with a FastAPI server over HTTP network requests.
----
## Features 
-**Add snippets:** create code snippets with custom titles, code content, and author handles (`--author`).
-**list and filter snippets:** view all stored snippets or filter specifically by author handles.
-**view snippet:** fetch complete snippet details using unique short IDs. 
-**delete snippets:** remove outdated or unwanted snippets by ID.
-**Robush Exception handling:** Network failure guards and HTTP error statuses
--
## Tech Stack
-**Add snippets:** python 3.x
-**API Framework:** FastAPI
-**ASGI Server:** uvicorn
-**HTTP client:** requests
-**data model validation:** pydantic
--
## quickstart amd usage
### 1. start the FastAPI server
'''bash
python -m uvicorn server:app --reload
### 2. RUN CLI command(In separate terminal)
**add a new snippet:
python cli.py add --title "array reverse" --code "arr.reverse()" --author "yashvi"
**list all the snippets:
python cli.py list
**filter snippets by author:
python cli.py list --author "yashvi"
**get the snippet by ID:
python cli.py get<SNIPPET_ID>
**delete a snippet by ID:
python cli.py delete <SNIPPET_ID>

