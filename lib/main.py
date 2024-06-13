#!/usr/bin/env python3
# lib/main.py
from commands import create_user_command, create_snippet_command, view_snippet_command, update_snippet_command, delete_snippet_command, search_snippets_command, list_snippets_command, list_collections_command

def parse_command(command):
    """
    Parse the user command and return the corresponding command function and arguments.

    Args:
        command (str): The user command string.

    Returns:
        tuple: A tuple containing the command function and its arguments.

    Raises:
        ValueError: If the command is invalid or the arguments are missing or incorrect.
    """
    parts = command.split()
    if len(parts) == 0:
        return None, []

    cmd = parts[0].lower()
    args = parts[1:]

    if cmd == "user":
        if len(args) != 1:
            raise ValueError("Usage: user <username>")
        return create_user_command, args
    elif cmd == "add":
        if len(args) != 3:
            raise ValueError("Usage: add <title> <language> <code>")
        return create_snippet_command, args
    elif cmd == "view":
        if len(args) != 1:
            raise ValueError("Usage: view <snippet_id>")
        return view_snippet_command, args
    elif cmd == "update":
        if len(args) != 3:
            raise ValueError("Usage: update <snippet_id> <field> <new_value>")
        return update_snippet_command, args
    elif cmd == "delete":
        if len(args) != 1:
            raise ValueError("Usage: delete <snippet_id>")
        return delete_snippet_command, args
    elif cmd == "search":
        if len(args) != 2:
            raise ValueError("Usage: search <field> <value>")
        return search_snippets_command, args
    elif cmd in ["list", "ls"]:
        if len(args) != 1:
            raise ValueError("Usage: list <snippets|collections>")
        if args[0] == "snippets":
            return list_snippets_command, []
        elif args[0] == "collections":
            return list_collections_command, []
        else:
            raise ValueError("Invalid argument for list command. Usage: list <snippets|collections>")
    else:
        raise ValueError(f"Unknown command: {cmd}")

def main():
    """
    The main function of the Code Marshall application.
    It displays the welcome message, prompts the user for commands, and executes the corresponding actions.
    """
    print("""

   _____          _        __  __                _           _ _ 
  / ____|        | |      |  \/  |              | |         | | |
 | |     ___   __| | ___  | \  / | __ _ _ __ ___| |__   __ _| | |
 | |    / _ \ / _` |/ _ \ | |\/| |/ _` | '__/ __| '_ \ / _` | | |
 | |___| (_) | (_| |  __/ | |  | | (_| | |  \__ \ | | | (_| | | |
  \_____\___/ \__,_|\___| |_|  |_|\__,_|_|  |___/_| |_|\__,_|_|_|
                                                                
                                                                

    """)
    print("Welcome to Code Marshall!")
    print("Enter 'help' to see available commands.")

    while True:
        try:
            command = input("Enter a command (or 'quit' to exit): ")
            if command.lower() == "quit":
                break
            elif command.lower() == "help":
                print_help()
            else:
                cmd_func, cmd_args = parse_command(command)
                cmd_func(*cmd_args)
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

def print_help():
    """
    Print the available commands and their usage instructions.
    """
    print("Available commands:")
    print("  user <username>                 Create a new user")
    print("  add <title> <language> <code>   Add a new code snippet")
    print("  view <snippet_id>               View a snippet")
    print("  update <snippet_id> <field> <new_value>  Update a snippet")
    print("  delete <snippet_id>             Delete a snippet")
    print("  search <field> <value>          Search snippets")
    print("  list snippets                   List all snippets")
    print("  list collections                List all collections")
    print("  quit                            Exit the application")

if __name__ == "__main__":
    main()