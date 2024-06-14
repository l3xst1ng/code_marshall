# lib/models.py
# lib/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        created_at (datetime): The timestamp indicating when the user was created.
        snippets (list): The code snippets associated with the user.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    snippets = relationship('Snippet', back_populates='user')

    def __init__(self, username):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
        """
        self.username = username

    @property
    def username(self):
        """
        Gets the username of the user.

        Returns:
            str: The username of the user.
        """
        return self._username

    @username.setter
    def username(self, value):
        """
        Sets the username of the user.

        Args:
            value (str): The new username value.

        Raises:
            ValueError: If the username is empty.
        """
        if not value:
            raise ValueError("Username cannot be empty.")
        self._username = value

class Collection(Base):
    """
    Represents a collection of code snippets.

    Attributes:
        id (int): The unique identifier of the collection.
        name (str): The name of the collection.
        snippets (list): The code snippets associated with the collection.
    """
    __tablename__ = 'collections'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    snippets = relationship('Snippet', back_populates='collection')

    def __init__(self, name):
        """
        Initialize a new Collection instance.

        Args:
            name (str): The name of the collection.
        """
        self.name = name

    @property
    def name(self):
        """
        Gets the name of the collection.

        Returns:
            str: The name of the collection.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the collection.

        Args:
            value (str): The new name value.

        Raises:
            ValueError: If the collection name is empty.
        """
        if not value:
            raise ValueError("Collection name cannot be empty.")
        self._name = value

class Snippet(Base):
    """
    Represents a code snippet.

    Attributes:
        id (int): The unique identifier of the snippet.
        title (str): The title of the snippet.
        description (str): The description of the snippet.
        language (str): The programming language of the snippet.
        code (str): The code content of the snippet.
        collection_id (int): The ID of the collection to which the snippet belongs.
        user_id (int): The ID of the user who owns the snippet.
        collection (Collection): The collection to which the snippet belongs.
        user (User): The user who owns the snippet.
    """
    __tablename__ = 'snippets'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    language = Column(String, nullable=False)
    code = Column(String, nullable=False)
    collection_id = Column(Integer, ForeignKey('collections.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    collection = relationship('Collection', back_populates='snippets')
    user = relationship('User', back_populates='snippets')

    def __init__(self, title, description, language, code, collection, user):
        """
        Initializes a new Snippet instance.

        Args:
            title (str): The title of the snippet.
            description (str): The description of the snippet.
            language (str): The programming language of the snippet.
            code (str): The code content of the snippet.
            collection (Collection): The collection to which the snippet belongs.
            user (User): The user who owns the snippet.
        """
        self.title = title
        self.description = description
        self.language = language
        self.code = code
        self.collection = collection
        self.user = user

    @property
    def title(self):
        """
        Gets the title of the snippet.

        Returns:
            str: The title of the snippet.
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Sets the title of the snippet.

        Args:
            value (str): The new title value.

        Raises:
            ValueError: If the title is empty.
        """
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def language(self):
        """
        Gets the programming language of the snippet.

        Returns:
            str: The programming language of the snippet.
        """
        return self._language

    @language.setter
    def language(self, value):
        """
        Sets the programming language of the snippet.

        Args:
            value (str): The new language value.

        Raises:
            ValueError: If the language is empty.
        """
        if not value:
            raise ValueError("Language cannot be empty.")
        self._language = value

    @property
    def code(self):
        """
        Gets the code content of the snippet.

        Returns:
            str: The code content of the snippet.
        """
        return self._code

    @code.setter
    def code(self, value):
        """
        Set the code content of the snippet.

        Args:
            value (str): The new code value.

        Raises:
            ValueError: If the code is empty.
        """
        if not value:
            raise ValueError("Code cannot be empty.")
        self._code = value

    @property
    def collection(self):
        """
        Gets the collection to which the snippet belongs.

        Returns:
            Collection: The collection to which the snippet belongs.
        """
        return self._collection

    @collection.setter
    def collection(self, value):
        """
        Sets the collection to which the snippet belongs.

        Args:
            value (Collection): The new collection value.

        Raises:
            ValueError: If the collection is not an instance of Collection.
        """
        if not isinstance(value, Collection):
            raise ValueError("Invalid collection. Expected an instance of Collection.")
        self._collection = value

    @property
    def user(self):
        """
        Gets the user who owns the snippet.

        Returns:
            User: The user who owns the snippet.
        """
        return self._user

    @user.setter
    def user(self, value):
        """
        Sets the user who owns the snippet.

        Args:
            value (User): The new user value.

        Raises:
            ValueError: If the user is not an instance of User.
        """
        if not isinstance(value, User):
            raise ValueError("Invalid user. Expected an instance of User.")
        self._user = value