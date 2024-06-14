# lib/config.py

import os

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db/snippets.db')

# Application configuration
APP_TITLE = "Code Marshall"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A command-line tool for managing code snippets."

# Logging configuration
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Command-line interface configuration
PROMPT = "Code Marshall> "
WELCOME_MESSAGE = f"""
 
   _____          _        __  __                _           _ _ 
  / ____|        | |      |  \/  |              | |         | | |
 | |     ___   __| | ___  | \  / | __ _ _ __ ___| |__   __ _| | |
 | |    / _ \ / _` |/ _ \ | |\/| |/ _` | '__/ __| '_ \ / _` | | |
 | |___| (_) | (_| |  __/ | |  | | (_| | |  \__ \ | | | (_| | | |
  \_____\___/ \__,_|\___| |_|  |_|\__,_|_|  |___/_| |_|\__,_|_|_|
 

Welcome to {APP_TITLE} v{APP_VERSION}!
{APP_DESCRIPTION}
Enter 'help' to see available commands.
"""

# Snippet configuration
MAX_SNIPPET_TITLE_LENGTH = 100
MAX_SNIPPET_DESCRIPTION_LENGTH = 500
MAX_SNIPPET_CODE_LENGTH = 5000

# Collection configuration
MAX_COLLECTION_NAME_LENGTH = 50

# User configuration
MAX_USERNAME_LENGTH = 20