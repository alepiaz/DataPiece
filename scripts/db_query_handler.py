"""
This module defines the DBQueryHandler class for handling database queries.
"""

import sqlite3
from scripts.utils.json import get_key_str
from scripts.utils.os import (
    file_exists_and_is_readable,
    file_exists_and_dir_is_writable,
    path_exists,
)
import os


class DBQueryHandler:
    """
    A handler for database queries.

    Attributes:
        schema_file (str): Path to the schema file.
        db_path (str): Path to the SQLite database file.
        delete_db (bool): Flag indicating whether to delete the existing database.
        conn (sqlite3.Connection): SQLite database connection.
        cursor (sqlite3.Cursor): SQLite database cursor.
    """

    def __init__(self, config: dict, delete_db: bool = False):
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
        self.handle_database_deletion()
        self.connect_to_database()
        self.create_database_if_needed()

    def handle_database_deletion(self):
        """
        Deletes the existing database file if needed and if the file is readable.
        """
        if self.need_to_delete() and file_exists_and_is_readable(self.db_path):
            os.remove(self.db_path)

    def need_to_delete(self):
        """
        Checks if the database should be deleted due to delete_db or test_mode being True.

        Returns:
            bool: True if deletion is needed, False otherwise.
        """

        return self.delete_db or self.test_mode

    def connect_to_database(self):
        """
        Connects to the SQLite database.
        """
        if file_exists_and_dir_is_writable(self.db_path) or not path_exists(
            self.db_path
        ):
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()

    def create_database_if_needed(self):
        """
        Creates the database schema if necessary.

        If the necessary tables do not exist in the database,
            it creates the database schema from the schema file.
        """
        if not self.check_tables():
            self.create_database(self.schema_file)

    def create_database(self, schema_file: str):
        """
        Creates the database schema if necessary.
        """
        self.initialize_database_from_schema(schema_file)

    def check_tables(self):
        """
        Checks if the necessary tables exist in the database.

        Returns:
            bool: True if the necessary tables exist, False otherwise.
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        return len(tables) > 0

    def initialize_database_from_schema(self, schema_file: str):
        """
        Initializes the database from the schema file.

        Parameters:
            schema_file (str): Path to the schema file.
        """
        sql_commands = self.load_commands_from_schema(schema_file)
        self.execute_sql_commands_list(sql_commands)

    def load_commands_from_schema(self, schema_file: str) -> list:
        """
        Loads the SQL commands from the schema file.

        Parameters:
            schema_file (str): Path to the schema file.

        Returns:
            list: List of SQL commands.
        """

        try:
            with open(schema_file, "r") as f:
                return f.read().split(";")
        except FileNotFoundError:
            print(f"Schema file {schema_file} does not exist.")
            return []

    def execute_sql_commands_list(self, sql_commands: list):
        """
        Executes the given list of SQL commands.

        Parameters:
            sql_commands (list): List of SQL commands.
        """
        for command in sql_commands:
            self.execute_sql_command(command)

    def execute_sql_command(self, command: str):
        """
        Executes the given SQL command.

        Parameters:
            command (str): SQL command.
        """
        try:
            self.cursor.execute(command)
        except sqlite3.OperationalError as e:
            print(f"Command skipped: {e}")

    def execute_query(self, query: str):
        """
        Executes the given SQL query and commits the changes.

        Parameters:
            query (str): SQL query.
        """
        self.cursor.execute(query)
        self.conn.commit()
