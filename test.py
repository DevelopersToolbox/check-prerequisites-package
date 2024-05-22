import sys

from wolfsoftware.prereqs import check_prerequisite, PrerequisiteCheckError

prerequisites: list[str] = ["python", "git", "youwontfindme"]

try:
    command_paths: dict = check_prerequisite(prerequisites)
except PrerequisiteCheckError as err:
    print("Prerequisite check failed:")
    for error in err.errors:
        print(error)
    sys.exit(1)

print(command_paths['python'])
