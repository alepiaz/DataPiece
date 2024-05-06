"""
A module for checking file and directory permissions.
"""

import os


def does_path_exist(path: str) -> bool:
    """
    Checks if a path exists.

    Args:
        path (str): Path to check.

    Returns:
        bool: True if path exists, False otherwise.
    """
    try:
        return os.path.exists(path)
    except OSError as e:
        print(f"An OSError occurred while checking if the file exists: {e}")
        return False


def is_path_readable(path: str) -> bool:
    """
    Checks if a path is readable.
    """
    try:
        return os.access(path, os.R_OK)
    except OSError as e:
        print(f"An OSError occurred while checking if the file is readable: {e}")
        return False


def is_path_writable(path: str) -> bool:
    """
    Checks if a path is writable.
    """
    try:
        return os.access(path, os.W_OK)
    except OSError as e:
        print(f"An OSError occurred while checking if the file is writable: {e}")
        return False


def can_read_existing_file(file_path: str) -> bool:
    """
    Checks if a file exists and is readable.
    """
    return does_path_exist(file_path) and is_path_readable(file_path)


def can_write_existing_file(file_path: str) -> bool:
    """
    Checks if a file exists and is writable.
    """
    return does_path_exist(file_path) and is_path_writable(file_path)


def can_write_to_dir_of_existing_file(file_path: str) -> bool:
    """
    Checks if a file exists and its directory is writable.
    """
    dir_path = os.path.dirname(file_path)
    return does_path_exist(file_path) and is_path_writable(dir_path)
