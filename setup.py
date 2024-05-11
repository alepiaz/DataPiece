"""
This module provides a console application that interacts with a database.

The application uses a configuration file to set up a console and a database query handler.
The console takes user input and uses the database query handler to interact with the database.
"""

import argparse
from argparse import Namespace
from typing import Any, Dict

from console import Console
from db_query_handler import DBQueryHandler
from utils.config import get_key_dict, load_config


def parse_arguments() -> Namespace:
    """
    Parses command-line arguments for the console application.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Start the console with a given config file."
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config/config.json",
        help="The path to the config file.",
    )
    parser.add_argument(
        "--delete-db",
        action="store_true",
        help="Delete the current database before starting the console.",
    )
    return parser.parse_args()


def create_handler(config: Dict[str, Any]) -> DBQueryHandler:
    """
    Creates a DBQueryHandler instance.

    Args:
        config (Dict[str, Any]): The configuration dictionary.

    Returns:
        DBQueryHandler: The created DBQueryHandler instance.
    """
    return DBQueryHandler(get_key_dict(config, "handler"))


def create_console(handler: DBQueryHandler, config: Dict[str, Any]) -> Console:
    """
    Creates a Console instance.

    Args:
        handler (DBQueryHandler): The DBQueryHandler instance.
        config (Dict[str, Any]): The configuration dictionary.

    Returns:
        Console: The created Console instance.
    """
    return Console(handler, get_key_dict(config, "console"))


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
