# pylint: disable=W1401  # Pylint doesn't appreciate fine art
# flake8: noqa  # Neither does flake8   ¯\_(ツ)_/¯
"""

                .---.        .-----------
               /     \  __  /    ------
              / /     \(  )/    -----
             //////   ' \/ `   ---
            //// / // :    : ---     CrowdStrike
           // /   /  /`    '--              FalconPy
          //          //..\\
                   _.UU8888UU8lkoz.,_
                d888888888888888888888b,
               j88P""V8888888888888888888
               888    8888888888888888888
               888baed8888888888888888888
               88888888888888888888888888
                            8888888888888
    ,ad8888888888888888888888888888888888  888888be,
   d8888888888888888888888888888888888888  888888888b,
  d88888888888888888888888888888888888888  8888888888b,
 j888888888888888888888888888888888888888  88888888888p,
j888888888888888888888888888888888888888'  8888888888888
8888888888888888888888888888888888888^"   ,8888888888888
88888888888888^'                        .d88888888888888
8888888888888"   .a8888888888888888888888888888888888888
8888888888888  ,888888888888888888888888888888888888888^
^888888888888  888888888888888888888888888888888888888^
 V88888888888  88888888888888888888888888888888888888Y
  V8888888888  8888888888888888888888888888888888888Y
   `"^8888888  8888888888888888888888888888888888^"'
               8888888888888
               88888888888888888888888888
               8888888888888888888P""V888
               8888888888888888888    888
               8888888888888888888baed88V
                `^888888888888888888888^
                  `'"^^V888888888V^^'

setup.py - PyPI packaging utility for CrowdStrike FalconPy
"""

from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import find_packages
from setuptools import setup
from src.falconpy import _VERSION, _MAINTAINER, _TITLE, _DESCRIPTION, _AUTHOR
from src.falconpy import _AUTHOR_EMAIL, _PROJECT_URL, _DOCS_URL, _KEYWORDS

with open("README.md", "r") as fh:
    long_description = fh.read()

# Remove GitHub's emoji
emojis = [":speech_balloon: ", ":bulb: ", ":pray: ", ":raised_hands: ", " :fire:", ":fire: ", "<small>", "</small>"]
for emoji in emojis:
    long_description = long_description.replace(emoji, "")

setup(
    name=_TITLE,
    version=_VERSION,
    author=_AUTHOR,
    author_email=_AUTHOR_EMAIL,
    maintainer=_MAINTAINER,
    maintainer_email=_AUTHOR_EMAIL,
    docs_url=_DOCS_URL,
    description=_DESCRIPTION,
    keywords=_KEYWORDS,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=_PROJECT_URL,
    project_urls = {
        "Documentation": "https://www.falconpy.io",
        "Source": "https://github.com/CrowdStrike/falconpy/tree/main/src/falconpy",
        "Tracker": "https://github.com/CrowdStrike/falconpy/issues"
    },
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    install_requires=[
        "requests",
        "urllib3"
    ],
    extras_require={
        "dev": [
            "flake8",
            "coverage",
            "pylint",
            "pytest-cov",
            "pytest",
            "bandit",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
)
