import argparse

from scripts.console import Console
from scripts.db_query_handler import DBQueryHandler
from scripts.utils.config import get_key_dict, load_config


def main():
    """
    The main function of the application. It does the following:

    1. Parses command-line arguments to get the path to the configuration file.
    2. Loads the configuration file.
    3. Creates an instance of the DBQueryHandler class with the handler configuration.
    4. Creates an instance of the Console class with the console configuration
        and the DBQueryHandler instance.
    5. Starts the console.

    If a RuntimeError occurs while starting the console,
        it catches the exception and prints an error message.
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
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        handler = DBQueryHandler(get_key_dict(config, "handler"))
        console = Console(handler, get_key_dict(config, "console"))
        console.start()
    except RuntimeError as e:
        print(f"An error occurred while starting the console: {e}")


if __name__ == "__main__":
    main()
