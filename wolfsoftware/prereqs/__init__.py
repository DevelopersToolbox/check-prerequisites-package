"""
This module provides functionality to check if the necessary prerequisite commands
are installed on the system. It includes custom exception handling to facilitate
error management in a more structured way.

Modules:
    prerequisite_checker: Contains the function check_prerequisite which checks for the
                          presence of specified commands.
    exceptions: Defines custom exceptions used in the package.

Functions:
    check_prerequisite(prerequisite_commands: list) -> dict:
        Checks if the specified prerequisite commands are installed on the system.
        Returns a dictionary mapping each command to its full path if found.
        Raises PrerequisiteCheckError if any commands are not found.

Exceptions:
    PrerequisiteCheckError:
        Raised when one or more prerequisite commands are not found.
        Contains a list of error messages detailing the missing commands.

Package Version:
    The package version is dynamically retrieved using importlib.metadata.version.
    If the package version cannot be found, it defaults to 'unknown'.

Usage Example:
    from wolfsoftware.prereqs import check_prerequisite, PrerequisiteCheckError

    prerequisites = ["python", "git", "nonexistent_command"]

    try:
        result = check_prerequisite(prerequisites)
        print("All prerequisites are installed:")
        print(result)
    except PrerequisiteCheckError as e:
        print("Prerequisite check failed:")
        for error in e.errors:
            print(error)

Attributes:
    __version__ (str): The version of the package.
    __all__ (list): A list of public objects of the module, as interpreted by import *.

"""

import importlib.metadata

from .prerequisite_checker import check_prerequisite
from .exceptions import PrerequisiteCheckError

try:
    __version__: str = importlib.metadata.version('wolfsoftware.prereqs')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__: list[str] = ['check_prerequisite', 'PrerequisiteCheckError']
