"""
This module provides a console interface for interacting with a database.
"""

from pyreadline3 import Readline
from scripts.db_query_handler import DBQueryHandler
from scripts.commands import Commands
from scripts.utils.json import get_key_dict


class Console:
    """
    A console interface for interacting with a database.

    Attributes:
        handler (DBQueryHandler): An instance of DBQueryHandler for handling database queries.
        config (dict): A configuration dictionary.
        commands_instance (Commands): An instance of Commands for handling commands.
        commands (list): A list of command names.
    """

    def __init__(self, handler: DBQueryHandler, config: dict):
        """
        The constructor for the Console class.

        Parameters:
            handler (DBQueryHandler): An instance of DBQueryHandler for handling database queries.
            config (dict): A configuration dictionary.
        """
        self.handler = handler
        self.config = config
        self.commands_instance = Commands(handler, get_key_dict(config, "commands"))
        self.commands = self.commands_instance.get_command_names()

    def start(self):
        """
        Starts the console interface.
        """
        readline = Readline()
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)

        print('Welcome to the SQL Console. Type "exit" to quit.')

        while True:
            try:
                command = readline.readline(">>> ")
                if command.lower().strip() == "exit":
                    break
                else:
                    command_parts = command.split()
                    command_name = command_parts[0]
                    if command_name in self.commands:
                        getattr(self.commands_instance, command_name)(
                            *command_parts[1:]
                        )
                    else:
                        print(f"Unknown command: {command_name}")
            except KeyboardInterrupt:
                # Handle Ctrl+C
                continue
            except EOFError:
                # Handle Ctrl+D / EOF
                break

        self.handler.conn.close()

    def completer(self, text: str, state: int):
        """
        Provides command completion options.

        Parameters:
            text (str): The current input text.
            state (int): The current completion state.

        Returns:
            str: A completion option that starts with the input text,
                or None if no more options are available.
        """
        options = [i for i in self.commands if i.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None
