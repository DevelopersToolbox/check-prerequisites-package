"""
Check if the necessary prerequisite commands are installed on the system.

It defines a function to verify the presence of specified commands and raises a
custom exception if any commands are not found.

Functions:
    check_prerequisite(prerequisite_commands: list) -> dict:
        Checks if the specified prerequisite commands are installed on the system.
        Returns a dictionary mapping each command to its full path if found.
        Raises PrerequisiteCheckError if any commands are not found.

Usage Example:
    from wolfsoftware.prereqs.prerequisite_checker import check_prerequisite
    from wolfsoftware.prereqs.exceptions import PrerequisiteCheckError

    prerequisites = ["python", "git", "nonexistent_command"]

    try:
        result = check_prerequisite(prerequisites)
        print("All prerequisites are installed:")
        print(result)
    except PrerequisiteCheckError as e:
        print("Prerequisite check failed:")
        for error in e.errors:
            print(error)

Functions:
    check_prerequisite(prerequisite_commands: list) -> dict:
        Checks if the specified prerequisite commands are installed on the system.
        - prerequisite_commands (list): A list of command names to check for.
        - Returns: A dictionary mapping each command to its full path if found.
        - Raises: PrerequisiteCheckError if any commands are not found.

Exceptions:
    PrerequisiteCheckError:
        Raised when one or more prerequisite commands are not found.
        Contains a list of error messages detailing the missing commands.

"""
# pylint: disable=relative-beyond-top-level

import shutil

from .exceptions import PrerequisiteCheckError


def check_prerequisite(prerequisite_commands: list) -> dict:
    """
    Check if the specified prerequisite commands are installed on the system.

    This function iterates through a list of command names, checking if each command
    is available on the system using the `shutil.which` method. If a command is found,
    its full path is added to the resulting dictionary. If any commands are not found,
    a PrerequisiteCheckError is raised with detailed error messages.

    Args:
        prerequisite_commands (list): A list of command names to check for installation.

    Returns:
        dict: A dictionary mapping each command to its full path if found.

    Raises:
        PrerequisiteCheckError: If one or more prerequisite commands are not found.
                                The error contains a list of messages detailing which
                                commands are missing.

    Usage Example:
        prerequisites = ["python", "git", "nonexistent_command"]

        try:
            result = check_prerequisite(prerequisites)
            print("All prerequisites are installed:")
            print(result)
        except PrerequisiteCheckError as e:
            print("Prerequisite check failed:")
            for error in e.errors:
                print(error)
    """
    errors_verbose: list = []
    command_paths: dict = {}

    for command in prerequisite_commands:
        full_path: str | None = shutil.which(command)
        if full_path is None:
            errors_verbose.append(f"{command} is not installed - Aborting")
        else:
            command_paths[command] = full_path

    if errors_verbose:
        raise PrerequisiteCheckError(errors_verbose)

    return command_paths
