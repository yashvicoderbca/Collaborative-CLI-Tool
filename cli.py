import argparse
import requests


# Base URL of the FastAPI backend
API_URL = "http://127.0.0.1:8000"


def add_command(args):
    """Create a new snippet through the REST API."""

    # Send the snippet title and code to the backend
    response = requests.post(
        f"{API_URL}/snippets",
        json={
            "title": args.title,
            "code": args.code
        }
    )

    # Handle a successful snippet creation
    if response.status_code == 200:
        data = response.json()

        print(data["message"])
        print(f"Snippet ID: {data['id']}")

    else:
        # Display the API error response
        print("Error:", response.text)


def list_command(args):
    """Retrieve and display all stored snippets."""

    # Request all snippets from the FastAPI backend
    response = requests.get(
        f"{API_URL}/snippets"
    )

    if response.status_code == 200:
        data = response.json()
        snippets = data["data"]

        # Handle the case where no snippets are available
        if not snippets:
            print("No snippets found.")
            return

        # The API returns snippets as a dictionary
        # where each key represents a snippet ID
        for snippet_id, snippet in snippets.items():
            print("-" * 40)
            print(f"ID: {snippet_id}")
            print(f"Title: {snippet.get('title')}")
            print(f"Code: {snippet.get('code')}")

    else:
        # Display the API error response
        print("Error:", response.text)


def get_command(args):
    """Retrieve and display a specific snippet by ID."""

    # Request the snippet using its unique ID
    response = requests.get(
        f"{API_URL}/snippets/{args.id}"
    )

    if response.status_code == 200:
        data = response.json()
        snippet = data["data"]

        print(f"ID: {snippet.get('id')}")
        print(f"Title: {snippet.get('title')}")
        print(f"Code: {snippet.get('code')}")

    else:
        # Display the API error response
        print("Error:", response.text)


def delete_command(args):
    """Delete a snippet using its unique ID."""

    # Send a DELETE request to the FastAPI backend
    response = requests.delete(
        f"{API_URL}/snippets/{args.id}"
    )

    if response.status_code == 200:
        data = response.json()

        print(data["message"])

    else:
        # Display the API error response
        print("Error:", response.text)


def main():
    """Configure CLI commands and process user input."""

    # Create the main command-line argument parser
    parser = argparse.ArgumentParser(
        description="Collaborative CLI Tool"
    )

    # Create subcommands for different snippet operations
    subparsers = parser.add_subparsers(
        dest="command"
    )

    # ---------------------------------------------------------
    # ADD command
    # ---------------------------------------------------------

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new snippet"
    )

    # Require a title for the new snippet
    add_parser.add_argument(
        "--title",
        required=True,
        help="Snippet title"
    )

    # Require the code content for the new snippet
    add_parser.add_argument(
        "--code",
        required=True,
        help="Snippet code"
    )

    # Connect the add command to its handler function
    add_parser.set_defaults(
        function=add_command
    )

    # ---------------------------------------------------------
    # LIST command
    # ---------------------------------------------------------

    list_parser = subparsers.add_parser(
        "list",
        help="List all snippets"
    )

    # Connect the list command to its handler function
    list_parser.set_defaults(
        function=list_command
    )

    # ---------------------------------------------------------
    # GET command
    # ---------------------------------------------------------

    get_parser = subparsers.add_parser(
        "get",
        help="Get a snippet by ID"
    )

    # Accept the snippet ID as a positional argument
    get_parser.add_argument(
        "id",
        help="Snippet ID"
    )

    # Connect the get command to its handler function
    get_parser.set_defaults(
        function=get_command
    )

    # ---------------------------------------------------------
    # DELETE command
    # ---------------------------------------------------------

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a snippet by ID"
    )

    # Accept the snippet ID as a positional argument
    delete_parser.add_argument(
        "id",
        help="Snippet ID"
    )

    # Connect the delete command to its handler function
    delete_parser.set_defaults(
        function=delete_command
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Execute the selected command if a valid command was provided
    if hasattr(args, "function"):
        args.function(args)

    else:
        # Show available commands when no command is provided
        parser.print_help()


# Run the CLI application when this file is executed directly
if __name__ == "__main__":
    main()
