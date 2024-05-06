"""
A module for handling JSON configuration files and checking file existence.
"""

import json
from typing import Any


def load_config(config_path: str) -> dict[str, Any]:
    """
    Loads a JSON config file.

    Args:
        config_path (str): Path to the config file.

    Returns:
        dict: Loaded config as a dictionary or an empty dictionary if file not found.
    """
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Config file {config_path} does not exist.")
        return {}
    return config


def get_key_dict(d: dict[str, Any], key: str) -> dict[str, Any]:
    """
    Returns the value of a key from a dictionary as a dict.
    """
    return d.get(key, {})


def get_key_str(d: dict[str, Any], key: str) -> str:
    """
    Returns the value of a key from a dictionary as a str.
    """
    return d.get(key, "")


def get_key_list(d: dict[str, Any], key: str) -> list[str]:
    """
    Returns the value of a key from a dictionary as a list.
    """
    return d.get(key, [])
