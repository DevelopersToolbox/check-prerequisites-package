"""
This module defines custom exceptions used in the wolfsoftware.prereqs package.

Currently, it includes a single exception class for handling errors related to
prerequisite command checks.

Classes:
    PrerequisiteCheckError(Exception):
        Custom exception raised when one or more prerequisite commands are not found.
        Contains a list of error messages detailing the missing commands.

Usage Example:
    from wolfsoftware.prereqs.exceptions import PrerequisiteCheckError

    try:
        raise PrerequisiteCheckError(["python is not installed", "git is not installed"])
    except PrerequisiteCheckError as e:
        print("Prerequisite check failed:")
        for error in e.errors:
            print(error)

Classes:
    PrerequisiteCheckError(Exception):
        Custom exception raised when one or more prerequisite commands are not found.
        - __init__(self, errors: list): Initializes the exception with a list of error messages.
        - errors (list): A list of error messages detailing the missing commands.

Attributes:
    errors (list): A list of error messages passed during the exception initialization.

"""


class PrerequisiteCheckError(Exception):
    """
    _summary_.

    _extended_summary_

    Arguments:
        Exception (_type_): _description_
    """

    def __init__(self, errors: list) -> None:
        """
        _summary_.

        _extended_summary_

        Arguments:
            errors (list): _description_
        """
        self.errors: list = errors
        super().__init__(f"{len(errors)} error(s) found: " + ", ".join(errors))
