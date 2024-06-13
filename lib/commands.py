# lib/commands.py
from database import Session
from models import User, Collection, Snippet

def create_user_command(username):
    """
    Creates a new user with the given username.

    Args:
        username (str): The username of the new user.

    Raises:
        ValueError: If the username is empty or invalid.
    """
    try:
        session = Session()
        user = User(username=username)
        session.add(user)
        session.commit()
        print(f"User '{username}' created successfully.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while creating the user: {str(e)}")
    finally:
        session.close()

def create_snippet_command(title, description, language, code, collection_name, username):
    """
    Creates a new code snippet with the given details.

    Args:
        title (str): The title of the snippet.
        description (str): The description of the snippet.
        language (str): The programming language of the snippet.
        code (str): The code content of the snippet.
        collection_name (str): The name of the collection to which the snippet belongs.
        username (str): The username of the user who owns the snippet.

    Raises:
        ValueError: If the user is not found or any of the input values are invalid.
    """
    try:
        session = Session()
        user = session.query(User).filter_by(username=username).first()
        if not user:
            raise ValueError(f"User '{username}' not found.")
        
        collection = session.query(Collection).filter_by(name=collection_name).first()
        if not collection:
            collection = Collection(name=collection_name)
            session.add(collection)
            session.commit()
        
        snippet = Snippet(title=title, description=description, language=language, code=code,
            collection=collection, user=user)
        session.add(snippet)
        session.commit()
        print("Snippet created successfully.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while creating the snippet: {str(e)}")
    finally:
        session.close()

def view_snippet_command(snippet_id):
    """
    Viewing the details of a code snippet with the given ID.

    Args:
        snippet_id (int): The ID of the snippet to view.

    Raises:
        ValueError: If the snippet with the given ID is not found.
    """
    try:
        session = Session()
        snippet = session.query(Snippet).filter_by(id=snippet_id).first()
        if not snippet:
            raise ValueError(f"Snippet with ID {snippet_id} not found.")
        
        print(f"Title: {snippet.title}")
        print(f"Description: {snippet.description}")
        print(f"Language: {snippet.language}")
        print(f"Code:\n{snippet.code}")
        print(f"Collection: {snippet.collection.name}")
        print(f"User: {snippet.user.username}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while viewing the snippet: {str(e)}")
    finally:
        session.close()

def update_snippet_command(snippet_id, title=None, description=None, language=None, code=None):
    """
    Updates the details of a code snippet with the given ID.

    Args:
        snippet_id (int): The ID of the snippet to update.
        title (str, optional): The new title of the snippet.
        description (str, optional): The new description of the snippet.
        language (str, optional): The new programming language of the snippet.
        code (str, optional): The new code content of the snippet.

    Raises:
        ValueError: If the snippet with the given ID is not found.
    """
    try:
        session = Session()
        snippet = session.query(Snippet).filter_by(id=snippet_id).first()
        if not snippet:
            raise ValueError(f"Snippet with ID {snippet_id} not found.")
        
        if title:
            snippet.title = title
        if description:
            snippet.description = description
        if language:
            snippet.language = language
        if code:
            snippet.code = code
        
        session.commit()
        print(f"Snippet with ID {snippet_id} updated successfully.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while updating the snippet: {str(e)}")
    finally:
        session.close()

def delete_snippet_command(snippet_id):
    """
    Deletes a code snippet with the given ID.

    Args:
        snippet_id (int): The ID of the snippet to delete.

    Raises:
        ValueError: If the snippet with the given ID is not found.
    """
    try:
        session = Session()
        snippet = session.query(Snippet).filter_by(id=snippet_id).first()
        if not snippet:
            raise ValueError(f"Snippet with ID {snippet_id} not found.")
        
        session.delete(snippet)
        session.commit()
        print(f"Snippet with ID {snippet_id} deleted successfully.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while deleting the snippet: {str(e)}")
    finally:
        session.close()

def search_snippets_command(language=None, collection_name=None, username=None):
    """
    Search for code snippets based on the given criteria.

    Args:
        language (str, optional): The specific snippet programming language to search for.
        collection_name (str, optional): The name of the collection to search in.
        username (str, optional): The username of the user whose snippets to search for.
    """
    try:
        session = Session()
        query = session.query(Snippet)
        
        if language:
            query = query.filter_by(language=language)
        if collection_name:
            query = query.join(Collection).filter(Collection.name == collection_name)
        if username:
            query = query.join(User).filter(User.username == username)
        
        snippets = query.all()
        if not snippets:
            print("No snippets found matching the search criteria.")
        else:
            print("Search Results:")
            for snippet in snippets:
                print(f"ID: {snippet.id}, Title: {snippet.title}, Language: {snippet.language}")
    except Exception as e:
        print(f"An error occurred while searching for snippets: {str(e)}")
    finally:
        session.close()

def list_snippets_command():
    """
    Listing all the code snippets.
    """
    try:
        session = Session()
        snippets = session.query(Snippet).all()
        if not snippets:
            print("No snippets found.")
        else:
            print("Snippets:")
            for snippet in snippets:
                print(f"ID: {snippet.id}, Title: {snippet.title}, Language: {snippet.language}")
    except Exception as e:
        print(f"An error occurred while listing snippets: {str(e)}")
    finally:
        session.close()

def list_collections_command():
    """
    Listing all the collections.
    """
    try:
        session = Session()
        collections = session.query(Collection).all()
        if not collections:
            print("No collections found.")
        else:
            print("Collections:")
            for collection in collections:
                print(f"ID: {collection.id}, Name: {collection.name}")
    except Exception as e:
        print(f"An error occurred while listing collections: {str(e)}")
    finally:
        session.close()