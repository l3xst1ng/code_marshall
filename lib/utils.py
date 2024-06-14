# lib/utils.py
import re

def validate_username(username):
    """
    Validates the username.

    Args:
        username (str): The username to validate.

    Raises:
        ValueError: If the username is empty, contains invalid characters, or has an invalid length.
    """
    if not username:
        raise ValueError("Username cannot be empty.")
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValueError("Username can only contain letters, digits, and underscores.")
    if len(username) < 3 or len(username) > 20:
        raise ValueError("Username must be between 3 and 20 characters long.")

def validate_collection_name(name):
    """
    Validates the collection name.

    Args:
        name (str): The collection name to validate.

    Raises:
        ValueError: If the collection name is empty, contains invalid characters, or has an invalid length.
    """
    if not name:
        raise ValueError("Collection name cannot be empty.")
    if not re.match(r'^[a-zA-Z0-9_\s]+$', name):
        raise ValueError("Collection name can only contain letters, digits, underscores, and spaces.")
    if len(name) < 3 or len(name) > 50:
        raise ValueError("Collection name must be between 3 and 50 characters long.")

def validate_snippet_title(title):
    """
    Validates the snippet title.

    Args:
        title (str): The snippet title to validate.

    Raises:
        ValueError: If the snippet title is empty or has an invalid length.
    """
    if not title:
        raise ValueError("Snippet title cannot be empty.")
    if len(title) < 3 or len(title) > 100:
        raise ValueError("Snippet title must be between 3 and 100 characters long.")

def validate_snippet_language(language):
    """
    Validates the snippet language.

    Args:
        language (str): The snippet language to validate.

    Raises:
        ValueError: If the snippet language is empty or contains invalid characters.
    """
    if not language:
        raise ValueError("Snippet language cannot be empty.")
    if not re.match(r'^[a-zA-Z0-9_\s]+$', language):
        raise ValueError("Snippet language can only contain letters, digits, underscores, and spaces.")

def validate_snippet_code(code):
    """
    Validates the snippet code.

    Args:
        code (str): The snippet code to validate.

    Raises:
        ValueError: If the snippet code is empty.
    """
    if not code:
        raise ValueError("Snippet code cannot be empty.")

def format_snippet(snippet):
    """
    Formats the snippet details.

    Args:
        snippet (Snippet): The snippet to format.

    Returns:
        str: The formatted snippet details.
    """
    formatted_snippet = f"ID: {snippet.id}\n"
    formatted_snippet += f"Title: {snippet.title}\n"
    formatted_snippet += f"Description: {snippet.description}\n"
    formatted_snippet += f"Language: {snippet.language}\n"
    formatted_snippet += f"Code:\n{snippet.code}\n"
    formatted_snippet += f"Collection: {snippet.collection.name}\n"
    formatted_snippet += f"User: {snippet.user.username}\n"
    return formatted_snippet

def format_snippet_list(snippets):
    """
    Formats the list of snippets.

    Args:
        snippets (list): The list of snippets to format.

    Returns:
        str: The formatted list of snippets.
    """
    formatted_list = "Snippets:\n"
    for snippet in snippets:
        formatted_list += f"ID: {snippet.id}, Title: {snippet.title}, Language: {snippet.language}\n"
    return formatted_list

def format_collection_list(collections):
    """
    Formats the list of collections.

    Args:
        collections (list): The list of collections to format.

    Returns:
        str: The formatted list of collections.
    """
    formatted_list = "Collections:\n"
    for collection in collections:
        formatted_list += f"ID: {collection.id}, Name: {collection.name}\n"
    return formatted_list