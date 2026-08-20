"""
Snippet Manager CLI
===================

Command-line interface for the local code snippet management system.

This module provides CLI commands to:
- Add a new code snippet
- List all stored snippets
- View a snippet by its ID
- Delete a snippet by its ID

The actual snippet storage and management logic is handled by
the `snippet_manager` module.

Usage:
    python cli.py add --title "Example" --code "print('Hello')"
    python cli.py list
    python cli.py view --id <snippet_id>
    python cli.py delete --id <snippet_id>

Author:
    Yashvi


"""
import argparse

from snippet_manager import add_snippet, list_snippets, get_snippet, delete_snippet


def main():
    # Setup command-line argument parser
    parser = argparse.ArgumentParser(
        description="Collaborative CLI tool-local snippet engine"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="available CLI commands"
    )

    # Command: add
    add_parser = subparsers.add_parser(
        "add",
        help="add a new code snippet"
    )
    add_parser.add_argument(
        "--title",
        required=True,
        help="title of the snippet"
    )
    add_parser.add_argument(
        "--code",
        required=True,
        help="code snippet content"
    )

    # Command: list
    subparsers.add_parser(
        "list",
        help="list all the local code snippets"
    )

    # Command: view
    view_parser = subparsers.add_parser(
        "view",
        help="view code snippet by ID"
    )
    view_parser.add_argument(
        "--id",
        required=True,
        help="snippet ID"
    )

    # Command: delete
    del_parser = subparsers.add_parser(
        "delete",
        help="delete a snippet by ID"
    )
    del_parser.add_argument(
        "--id",
        required=True,
        help="snippet ID"
    )

    args = parser.parse_args()

    # Route CLI command to snippet manager functions
    if args.command == "add":
        snippet_id = add_snippet(args.title, args.code)
        print(f"[SUCCESS] Snippet added successfully. ID: {snippet_id}")

    elif args.command == "list":
        snippets = list_snippets()

        if not snippets:
            print("[INFO] NO SNIPPETS FOUND.")
        else:
            print("\n--- Local Code Snippets ---")
            for s_id, data in snippets.items():
                print(f"ID: {s_id} | Title: {data['title']}")
                print("=======================================\n")

    elif args.command == "view":
        snippet = get_snippet(args.id)

        if snippet:
            print(
                f"\n--- Snippet: {snippet['title']} "
                f"(ID: {snippet['id']}) ---"
            )
            print(snippet["code"])
            print("------------------------------------------------------------\n")
        else:
            print(f"[ERROR] Snippet with ID '{args.id}' not found.")

    elif args.command == "delete":
        if delete_snippet(args.id):
            print(f"[SUCCESS] SNIPPET '{args.id}' deleted successfully.")
        else:
            print(f"[ERROR] SNIPPET with ID '{args.id}' not found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
