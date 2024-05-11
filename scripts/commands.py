"""
This module defines the Commands class which provides an interface for executing SQL commands.

TODO:
    * Add more command methods as needed.
    * Store temporary informations in a file
"""

from typing import Any

from scripts.db_query_handler import DBQueryHandler
from scripts.utils.config import get_key_list


class Commands:
    """
    A class for executing database commands.

    Attributes:
        handler (DBQueryHandler): Executes the queries.
    """

    def __init__(self, handler: DBQueryHandler, config: dict[str, Any]) -> None:
        """
        Constructs all the necessary attributes for the Commands object.

        Args:
            handler (DBQueryHandler): An instance of DBQueryHandler to execute the queries.
            config (dict): A dictionary containing config information for commands
        """
        self.handler = handler
        self.config = config
        self.exclude_list = get_key_list(config, "exclude_list")

    def get_command_names(self) -> list[str]:
        """
        Get a list of command names that are not exlcuded (i.e. __init__).

        Returns:
            list[str]: A list of commands
        """
        return [func for func in dir(self) if self._is_valid_command(func)]

    def _is_valid_command(self, func: str) -> bool:
        """
        Check if the method with the given name is callable and not excluded.
        """
        return callable(getattr(self, func)) and func not in self.exclude_list

    def start_volume(self, volume_number: int) -> None:
        """
        Inserts a new volume with the given volume number into the 'Volumes' table.

        Args:
            volume_number (int): The number of the volume to be started.
        """
        query = f"INSERT INTO  `Volumes` (`VolumeNumber`) VALUES ({volume_number})"
        self.handler.execute_query(query)
