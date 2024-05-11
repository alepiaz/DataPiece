"""
This module defines the DBQueryHandler class for handling database queries.
"""

import os
import sqlite3

from scripts.utils.config import get_key_str
from scripts.utils.files import (
    is_path_existent,
    is_readable_existing_file,
    is_writeable_file_directory,
)


class DBQueryHandler:  # pylint: disable=too-few-public-methods
    """
    A handler for database queries.

    Attributes:
        schema_file (str): Path to the schema file.
        db_path (str): Path to the SQLite database file.
        delete_db (bool): Flag indicating whether to delete the existing database.
        conn (sqlite3.Connection): SQLite database connection.
        cursor (sqlite3.Cursor): SQLite database cursor.
    """

    def __init__(self, config: dict, delete_db: bool = False) -> None:
        """
        Initializes the DBQueryHandler with the given configuration and deletion flag.

        Parameters:
            config (dict): Configuration dictionary.
            delete_db (bool): Deletion flag.
        """
        self.schema_file = get_key_str(config, "schema")
        self.db_path = get_key_str(config, "db")
        self.test_mode = get_key_str(config, "mode") == "test"
        self.delete_db = delete_db
        self._handle_database_deletion()
        self._connect_to_database()
        self._create_database_if_not_exist()

    def _handle_database_deletion(self) -> None:
        """
        Deletes the existing database file if needed and if the file is readable.
        """
        if self._is_need_to_delete() and is_readable_existing_file(self.db_path):
            os.remove(self.db_path)

    def _is_need_to_delete(self) -> bool:
        """
        Checks if the database should be deleted due to delete_db or test_mode being True.

        Returns:
            bool: True if deletion is needed, False otherwise.
        """
        return self.delete_db or self.test_mode

    def _connect_to_database(self) -> None:
        """
        Connects to the SQLite database.
        """
        if is_writeable_file_directory(self.db_path) or not is_path_existent(
            self.db_path
        ):
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()

    def _create_database_if_not_exist(self) -> None:
        """
        Creates the database schema if necessary.

        If the necessary tables do not exist in the database,
            it creates the database schema from the schema file.
        """
        if not self._check_tables_existence():
            self._create_database(self.schema_file)

    def _create_database(self, schema_file: str) -> None:
        """
        Creates the database schema if necessary.

        Args:
            schema_file (str): The path to the schema file containing
                the database schema definition.
        """
        self._initialize_database_from_schema(schema_file)

    def _check_tables_existence(self) -> int:
        """
        Checks if the necessary tables exist in the database.

        Returns:
            bool: True if the necessary tables exist, False otherwise.
        """
        self.cursor.execute("SELECT `name` FROM `sqlite_master` WHERE `type`='table'")
        tables = self.cursor.fetchall()
        return len(tables) > 0

    def _initialize_database_from_schema(self, schema_file: str) -> None:
        """
        Initializes the database from the schema file.

        Parameters:
            schema_file (str): Path to the schema file.
        """
        sql_commands = self._load_commands_from_schema(schema_file)
        self._execute_sql_commands_list(sql_commands)

    def _load_commands_from_schema(self, schema_file: str) -> list[str]:
        """
        Loads the SQL commands from the schema file.

        Parameters:
            schema_file (str): Path to the schema file.

        Returns:
            list[str]: List of SQL commands.
        """
        try:
            with open(schema_file, "r", encoding="utf-8") as f:
                return f.read().split(";")
        except FileNotFoundError:
            print(f"Schema file {schema_file} does not exist.")
            return []

    def _execute_sql_commands_list(self, sql_commands: list[str]) -> None:
        """
        Executes the given list of SQL commands and commits the changes.

        Parameters:
            sql_commands (list): List of SQL commands.
        """
        for command in sql_commands:
            self.execute_query(command, commit=False)
        self.conn.commit()

    def execute_query(self, query: str, commit=True) -> None:
        """
        Executes the given SQL query and commits the changes.

        Parameters:
            query (str): SQL query.
        """
        self.cursor.execute(query)
        if commit:
            self.conn.commit()
