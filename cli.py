import argparse
import requests


# Base URL of the FastAPI backend
API_URL = "http://127.0.0.1:8000"


def add_command(args):
    """Create a new snippet with an author tag."""

    payload = {
        "title": args.title,
        "code": args.code,
        "author": args.author
    }

    try:
        response = requests.post(
            f"{API_URL}/snippets",
            json=payload
        )

        if response.status_code == 200:
            data = response.json()

            print("\n[SUCCESS] Snippet created successfully!")
            print(f"ID     : {data['id']}")
            print(f"Title  : {args.title}")
            print(f"Author : {args.author}")
            print(f"Code   : {args.code}")
            print()

        else:
            print("[ERROR]", response.text)

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the FastAPI server.")
        print(
            "Please start the server using: "
            "python -m uvicorn server:app --reload"
        )


def list_command(args):
    """Retrieve and display snippets, optionally filtered by author."""

    params = {}

    if args.author:
        params["author"] = args.author

    try:
        response = requests.get(
            f"{API_URL}/snippets",
            params=params
        )

        if response.status_code == 200:
            data = response.json()
            snippets = data.get("data", {})

            if not snippets:
                print("[INFO] No snippets found.")
                return

            print("\n========== CODE SNIPPETS ==========\n")

            for snippet_id, snippet in snippets.items():

                author = snippet.get(
                    "author",
                    "Anonymous"
                )

                print(f"ID     : {snippet_id}")
                print(f"Title  : {snippet.get('title')}")
                print(f"Author : {author}")
                print(f"Code   : {snippet.get('code')}")
                print("-" * 40)

        else:
            print("[ERROR]", response.text)

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the FastAPI server.")


def get_command(args):
    """Retrieve and display a specific snippet by ID."""

    try:
        response = requests.get(
            f"{API_URL}/snippets/{args.id}"
        )

        if response.status_code == 200:

            snippet = response.json().get(
                "data",
                {}
            )

            print("\n========== SNIPPET ==========")
            print(f"ID     : {snippet.get('id')}")
            print(f"Title  : {snippet.get('title')}")
            print(
                f"Author : "
                f"{snippet.get('author', 'Anonymous')}"
            )
            print(f"Code   : {snippet.get('code')}")
            print("==============================\n")

        else:
            print("[ERROR]", response.text)

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the FastAPI server.")


def delete_command(args):
    """Delete a snippet using its unique ID."""

    try:
        response = requests.delete(
            f"{API_URL}/snippets/{args.id}"
        )

        if response.status_code == 200:

            data = response.json()

            print(
                f"[SUCCESS] {data['message']}"
            )

        else:
            print("[ERROR]", response.text)

    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not connect to the FastAPI server.")


def main():

    parser = argparse.ArgumentParser(
        description="Collaborative CLI Tool"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # =========================
    # ADD COMMAND
    # =========================

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new snippet"
    )

    add_parser.add_argument(
        "--title",
        required=True,
        help="Snippet title"
    )

    add_parser.add_argument(
        "--code",
        required=True,
        help="Snippet code"
    )

    add_parser.add_argument(
        "--author",
        default="Anonymous",
        help="Author handle"
    )

    add_parser.set_defaults(
        function=add_command
    )

    # =========================
    # LIST COMMAND
    # =========================

    list_parser = subparsers.add_parser(
        "list",
        help="List all snippets"
    )

    list_parser.add_argument(
        "--author",
        help="Filter snippets by author"
    )

    list_parser.set_defaults(
        function=list_command
    )

    # =========================
    # GET COMMAND
    # =========================

    get_parser = subparsers.add_parser(
        "get",
        help="Get a snippet by ID"
    )

    get_parser.add_argument(
        "id",
        help="Snippet ID"
    )

    get_parser.set_defaults(
        function=get_command
    )

    # =========================
    # DELETE COMMAND
    # =========================

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a snippet by ID"
    )

    delete_parser.add_argument(
        "id",
        help="Snippet ID"
    )

    delete_parser.set_defaults(
        function=delete_command
    )

    # Parse arguments
    args = parser.parse_args()

    # Execute selected command
    if hasattr(args, "function"):
        args.function(args)
    else:
        parser.print_help()


# Start CLI application
if __name__ == "__main__":
    main()
