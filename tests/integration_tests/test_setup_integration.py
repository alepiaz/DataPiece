"""
This module contains integration tests for the setup
"""

import json
import os
import sqlite3
import unittest


class TestSetupIntegration(unittest.TestCase):
    """
    This class contains integration tests for the setup
    """

    def setUp(self) -> None:
        """
        This method sets up the environment for each test.
        It creates a test database and a test configuration file.
        """
        self.db_path = "test_db.sqlite"
        self.config_path = "test_config.json"
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump({"handler": {"db_path": self.db_path}, "console": {}}, f)

    def tearDown(self) -> None:
        """
        This method cleans up the environment after each test.
        It removes the test database and the test configuration file.
        """
        os.remove(self.db_path)
        os.remove(self.config_path)

    def test_main(self) -> None:
        """
        This method tests the main function of the setup.
        It runs the application with the test configuration file,
            then checks if the database is correctly set up
            by querying the database and checking it's e,pty.
        """
        os.system(f"python setup.py --config {self.config_path}")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        records = cursor.fetchall()
        print(records)
        conn.close()

        self.assertEqual(len(records), 0)


if __name__ == "__main__":
    unittest.main()
