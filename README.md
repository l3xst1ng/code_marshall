

# Code Marshall

Welcome to Code Marshall! This command-line application is designed to help users easily store, organize, and manage your code snippets. Whether you're a programmer, a developer, or just someone who loves to collect useful pieces of code, this tool is perfect for you.

## Features

- **User-Friendly Interface**: Interact with the application through a simple and intuitive command-line interface.
- **Snippet Creation**: Easily add new code snippets by providing a title, language, and the code itself.
- **Snippet Organization**: Organize your snippets into collections or categories for better management.
- **Snippet Retrieval**: Quickly search and retrieve snippets based on language, collection, or user.
- **Snippet Manipulation**: Update or delete snippets as needed.
- **User Management**: Create and manage multiple users, each with their own set of snippets.
- **Data Persistence**: All your snippets and collections are securely stored in a SQLite database.

## Installation

1. Make sure you have Python installed on your system. You can download it from the official Python website: [https://www.python.org](https://www.python.org)

2. Clone this repository to your local machine or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

5. Make the `main.py` file executable by running the following command:
   ```
   chmod +x lib/main.py
   ```

6. You're all set! Code Marshall is now ready to use.

## Usage

To start the application, open a terminal or command prompt, navigate to the project directory, and run the following command:
```
./lib/main.py
```

When you run the application, you will see the "Code Marshall" app title intro followed by a welcome message and the command-line interface:

```

  _____          _        __  __                _           _ _ 
  / ____|        | |      |  \/  |              | |         | | |
 | |     ___   __| | ___  | \  / | __ _ _ __ ___| |__   __ _| | |
 | |    / _ \ / _` |/ _ \ | |\/| |/ _` | '__/ __| '_ \ / _` | | |
 | |___| (_) | (_| |  __/ | |  | | (_| | |  \__ \ | | | (_| | | |
  \_____\___/ \__,_|\___| |_|  |_|\__,_|_|  |___/_| |_|\__,_|_|_|
                                                                 
Welcome to Code Marshall!
Enter 'help' to see available commands.
```

You can enter various commands to interact with the application. Here are some of the available commands:

- `user <username>`: Create a new user with the specified username.
- `add <title> <language> <code>`: Add a new code snippet with the given title, language, and code.
- `view <snippet_id>`: View the details of a snippet with the specified ID.
- `update <snippet_id> <field> <new_value>`: Update a specific field (title, language, or code) of a snippet with the given ID.
- `delete <snippet_id>`: Delete a snippet with the specified ID.
- `search <field> <value>`: Search for snippets based on a specific field (language, collection, or user) and its value.

For a complete list of available commands and their usage, type `help` in the application.

## Examples

Here are a few examples to help you get started:

1. Create a new user:
   ```
   user john_doe
   ```

2. Add a new code snippet:
   ```
   add "Python List Comprehension" Python "squares = [x**2 for x in range(10)]"
   ```

3. View a snippet:
   ```
   view 1
   ```

4. Update a snippet's title:
   ```
   update 1 title "Updated Title"
   ```

5. Delete a snippet:
   ```
   delete 1
   ```

6. Search snippets by language:
   ```
   search language Python
   ```

Feel free to explore and experiment with the various commands to manage your code snippets efficiently.

## Contributing

If you'd like to contribute to Code Marshall, you can:

- Report bugs or suggest improvements by opening an issue on the GitHub repository.
- Fork the repository, make your changes, and submit a pull request.

We appreciate your contributions!

## License

This project is licensed under the [MIT License].

## Contact

If you have any questions, suggestions, or feedback.

Happy coding and snippet managing with Code Marshall!

