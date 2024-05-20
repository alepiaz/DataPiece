"""
Unit tests for the Commands class.
"""

import unittest
from unittest.mock import Mock, create_autospec

from scripts.commands import Commands
from scripts.db_query_handler import DBQueryHandler


class TestCommands(unittest.TestCase):
    """
    Test case for the Commands class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.handler = create_autospec(DBQueryHandler)
        self.handler.conn = Mock()
        self.config = {"exclude_list": ["__init__"]}
        self.commands = Commands(self.handler, self.config)

    def test_get_command_names(self):
        """
        Test the get_command_names method.
        """
        command_names = self.commands.get_command_names()
        self.assertIsInstance(command_names, list)
        self.assertNotIn("__init__", command_names)

    def test_is_valid_command(self):
        """
        Test the _is_valid_command method.
        """
        # pylint: disable=protected-access
        self.assertFalse(self.commands._is_valid_command("__init__"))
        self.assertTrue(self.commands._is_valid_command("start_volume"))

    def test_start_volume(self):
        """
        Test the start_volume method.
        """
        volume_number = 1
        self.commands.start_volume(volume_number)
        self.handler.execute_query.assert_called_once_with(
            f"INSERT INTO `Volumes` (`VolumeNumber`) VALUES ({volume_number})"
        )
        self.handler.conn.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
