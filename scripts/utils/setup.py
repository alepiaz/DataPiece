"""
This module provides utility functions for the setup of the application.
"""

from argparse import ArgumentParser, Namespace
from typing import Any, Dict

from scripts.console import Console
from scripts.db_query_handler import DBQueryHandler
from scripts.utils.config import get_key_dict


def parse_arguments() -> Namespace:
    """
    Parses command-line arguments for the console application.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = ArgumentParser(description="Start the console with a given config file.")
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
