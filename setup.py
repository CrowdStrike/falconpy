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

from setuptools import find_packages
from setuptools import setup
from glob import glob
from os.path import basename
from os.path import splitext
from src.falconpy import _version, _maintainer, _title, _description, _author, _author_email, _project_url

with open("README.md", "r") as fh:
    long_description = fh.read()

# Remove GitHub's emoji
emojis = [":speech_balloon: ", ":bulb: ", ":pray: ", ":raised_hands: ", " :fire:", ":fire: "]
for emoji in emojis:
    long_description = long_description.replace(emoji, "")

setup(
    name=_title,
    version=_version,
    author=_author,
    author_email=_author_email,
    maintainer=_maintainer,
    description=_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=_project_url,
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
