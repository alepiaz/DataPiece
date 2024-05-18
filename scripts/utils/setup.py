"""
This module provides utility functions for the setup of the application.
"""

from typing import Any, Dict

from scripts.console import Console
from scripts.db_query_handler import DBQueryHandler
from scripts.utils.config import get_key_dict


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
