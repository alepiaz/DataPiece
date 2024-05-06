"""
A module for checking file and directory permissions.
"""

import os


def path_exists(path):
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


def path_is_readable(path):
    """
    Checks if a path is readable.
    """
    try:
        return os.access(path, os.R_OK)
    except OSError as e:
        print(f"An OSError occurred while checking if the file is readable: {e}")
        return False


def path_is_writable(path):
    """
    Checks if a path is writable.
    """
    try:
        return os.access(path, os.W_OK)
    except OSError as e:
        print(f"An OSError occurred while checking if the file is writable: {e}")
        return False


def file_exists_and_is_readable(file_path):
    """
    Checks if a file exists and is readable.
    """
    return path_exists(file_path) and path_is_readable(file_path)


def file_exists_and_is_writable(file_path):
    """
    Checks if a file exists and is writable.
    """
    return path_exists(file_path) and path_is_writable(file_path)


def file_exists_and_dir_is_writable(file_path):
    """
    Checks if a file exists and its directory is writable.
    """
    dir_path = os.path.dirname(file_path)
    return path_exists(file_path) and path_is_writable(dir_path)
