<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/DevelopersToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/developerstoolbox/black-and-white-circle-256.png" alt="DevelopersToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/DevelopersToolbox/check-prerequisite/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/DevelopersToolbox/check-prerequisite?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite">
        <img src="https://img.shields.io/github/created-at/DevelopersToolbox/check-prerequisite?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/releases/latest">
        <img src="https://img.shields.io/github/v/release/DevelopersToolbox/check-prerequisite?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/releases/latest">
        <img src="https://img.shields.io/github/release-date/DevelopersToolbox/check-prerequisite?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/releases/latest">
        <img src="https://img.shields.io/github/commits-since/DevelopersToolbox/check-prerequisite/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/DevelopersToolbox/check-prerequisite/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

When you write a script or tool which uses subprocess to execute shell commands, you want to know if the commands are installed or not. This is
particularly important if you are running multiple commands which rely on each other.

You can of course catch the exceptions through using `check=True` but if you need to know they all exist before you start your execution run then
this doesn't help you as it only handled the failure it currently has.

This little package assist with that problem by taking a list of commands that must be installed and available and verifies that list at the start to
ensure all of them are available.

## Installation

```shell
pip install wolfsoftware.prereqs
```

## Usage

```python
import sys

from wolfsoftware.prereqs import check_prerequisite, PrerequisiteCheckError

prerequisites: list[str] = ["python", "git"]

try:
    command_paths: dict = check_prerequisite(prerequisites)
except PrerequisiteCheckError as err:
    print("Prerequisite check failed:")
    for error in e.errors:
        print(error)
    sys.exit(0)

print(command_paths['python'])
```

Once the checks have completed, you now have a dict of commands and their associated paths which you can then utilise to ensure you are executing
your subprocesses with the full path.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
