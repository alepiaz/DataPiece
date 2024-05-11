"""
This module contains unit tests for the setup
"""

import unittest
from unittest.mock import MagicMock, patch

from setup import create_console, create_handler, parse_arguments
import sys


class TestSetupUnit(unittest.TestCase):
    """
    This class contains unit tests for the setup
    """

    def setUp(self) -> None:
        """debug"""
        for path in sys.path:
            print(path)

    @patch("argparse.ArgumentParser.parse_args")
    def test_parse_arguments(self, mock_parse_args: MagicMock):
        """
        Test the parse_arguments function.

        This test checks if the function correctly parses command-line arguments.
        """
        mock_parse_args.return_value = MagicMock()
        args = parse_arguments()
        self.assertEqual(args, mock_parse_args.return_value)

    @patch("setup.DBQueryHandler")
    def test_create_handler(self, mock_db_query_handler: MagicMock):
        """
        Test the create_handler function.

        This test checks if the function correctly creates a DBQueryHandler instance.
        """
        config = {"handler": {"key": "value"}}
        handler = create_handler(config)
        mock_db_query_handler.assert_called_once_with({"key": "value"})
        self.assertEqual(handler, mock_db_query_handler.return_value)

    @patch("setup.Console")
    def test_create_console(self, mock_console):
        """
        Test the create_console function.

        This test checks if the function correctly creates a Console instance.
        """
        handler = MagicMock()
        config = {"console": {"key": "value"}}
        console = create_console(handler, config)
        mock_console.assert_called_once_with(handler, {"key": "value"})
        self.assertEqual(console, mock_console.return_value)


if __name__ == "__main__":
    unittest.main()
