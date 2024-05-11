"""
This module provides a console application that interacts with a database.

The application uses a configuration file to set up a console and a database query handler.
The console takes user input and uses the database query handler to interact with the database.
"""

from scripts.utils.config import load_config
from scripts.utils.setup import create_console, create_handler, parse_arguments


def main() -> None:
    """
    The main function of the application. It does the following:

    1. Parses command-line arguments.
    2. Loads the configuration file.
    3. Creates an instance of the DBQueryHandler class.
    4. Creates an instance of the Console class.
    5. Starts the console.

    If a RuntimeError occurs while starting the console,
        it catches the exception and prints an error message.
    """
    args = parse_arguments()
    config = load_config(args.config)
    handler = create_handler(config)
    console = create_console(handler, config)

    try:
        console.start()
    except RuntimeError as error:
        print(f"An error occurred while starting the console: {error}")


if __name__ == "__main__":
    main()
