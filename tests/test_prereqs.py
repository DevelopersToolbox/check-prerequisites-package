"""
test_prereqs.py

This module contains test cases for the wolfsoftware.prereqs package. It uses pytest
to validate the functionality of the check_prerequisite function and the custom
PrerequisiteCheckError exception.

The tests cover various scenarios including:
- All prerequisites installed
- Some prerequisites missing
- All prerequisites missing
- An empty list of prerequisites

Functions:
    test_all_prerequisites_installed(mocker):
        Tests if the check_prerequisite function correctly identifies all installed commands.

    test_some_prerequisites_missing(mocker):
        Tests if the check_prerequisite function raises PrerequisiteCheckError when some commands are missing.

    test_all_prerequisites_missing(mocker):
        Tests if the check_prerequisite function raises PrerequisiteCheckError when all commands are missing.

    test_empty_prerequisites_list():
        Tests if the check_prerequisite function returns an empty dictionary when no prerequisites are specified.

Usage Example:
    To run these tests, navigate to the directory containing this file and execute:

        pytest

Dependencies:
    pytest: The testing framework used to write and run the test cases.
    pytest-mock: A pytest plugin that provides support for mocking, required for mocker.

"""

import pytest

from wolfsoftware.prereqs import check_prerequisite, PrerequisiteCheckError  # pylint: disable=import-error


def test_all_prerequisites_installed(mocker) -> None:
    """
    Test case for when all prerequisite commands are installed.

    This test checks that the check_prerequisite function correctly identifies
    that all specified commands (in this case, "python" and "git") are installed
    on the system. It mocks shutil.which to return valid paths for these commands
    and verifies that the function returns the expected dictionary of command paths.

    Args:
        mocker: The mocker fixture provided by pytest-mock to mock the behaviour
                of shutil.which.

    Returns:
        None

    Raises:
        AssertionError: If the function does not return the expected result.
    """
    # Mock shutil.which to return valid paths
    mocker.patch('shutil.which', side_effect=lambda cmd: f"/usr/bin/{cmd}" if cmd in ["python", "git"] else None)

    prerequisites: list[str] = ["python", "git"]
    expected_result: dict[str, str] = {
        "python": "/usr/bin/python",
        "git": "/usr/bin/git"
    }
    assert check_prerequisite(prerequisites) == expected_result  # nosec: B101


def test_some_prerequisites_missing(mocker) -> None:
    """
    Test case for when some prerequisite commands are missing.

    This test checks that the check_prerequisite function raises a PrerequisiteCheckError
    when some specified commands (in this case, "git") are not installed on the system.
    It mocks shutil.which to return None for the missing command and verifies that the
    exception contains the correct error message.

    Args:
        mocker: The mocker fixture provided by pytest-mock to mock the behaviour
                of shutil.which.

    Returns:
        None

    Raises:
        AssertionError: If the function does not raise the expected exception or
                        if the exception does not contain the correct error message.
    """
    # Mock shutil.which to return None for missing commands
    mocker.patch('shutil.which', side_effect=lambda cmd: f"/usr/bin/{cmd}" if cmd == "python" else None)

    prerequisites: list[str] = ["python", "git"]
    with pytest.raises(PrerequisiteCheckError) as exc_info:
        check_prerequisite(prerequisites)

    assert len(exc_info.value.errors) == 1  # nosec: B101
    assert exc_info.value.errors[0] == "git is not installed - Aborting"  # nosec: B101


def test_all_prerequisites_missing(mocker) -> None:
    """
    Test case for when all prerequisite commands are missing.

    This test checks that the check_prerequisite function raises a PrerequisiteCheckError
    when all specified commands (in this case, "python" and "git") are not installed on
    the system. It mocks shutil.which to return None for all commands and verifies that
    the exception contains the correct error messages.

    Args:
        mocker: The mocker fixture provided by pytest-mock to mock the behaviour
                of shutil.which.

    Returns:
        None

    Raises:
        AssertionError: If the function does not raise the expected exception or
                        if the exception does not contain the correct error messages.
    """
    # Mock shutil.which to return None for all commands
    mocker.patch('shutil.which', return_value=None)

    prerequisites: list[str] = ["python", "git"]
    with pytest.raises(PrerequisiteCheckError) as exc_info:
        check_prerequisite(prerequisites)

    assert len(exc_info.value.errors) == 2  # nosec: B101
    assert "python is not installed - Aborting" in exc_info.value.errors  # nosec: B101
    assert "git is not installed - Aborting" in exc_info.value.errors  # nosec: B101


def test_empty_prerequisites_list() -> None:
    """
    Test case for an empty list of prerequisite commands.

    This test checks that the check_prerequisite function returns an empty dictionary
    when no prerequisite commands are specified. This verifies that the function
    handles an empty input list correctly.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the function does not return an empty dictionary.
    """

    assert not check_prerequisite([])  # nosec: B101
