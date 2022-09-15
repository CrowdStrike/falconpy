r"""

                .---.        .-----------
               /     \  __  /    ------
              / /     \(..)/    -----
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

dev_setup.py - PyPI packaging utility for CrowdStrike FalconPy (Development Package)
"""
from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import find_packages
from setuptools import setup
from src.falconpydev import _VERSION, _MAINTAINER, _TITLE, _DESCRIPTION, _AUTHOR
from src.falconpydev import _AUTHOR_EMAIL, _PROJECT_URL, _DOCS_URL, _KEYWORDS


LOGO = []
LOGO.append("![Development Package]")
LOGO.append("(https://img.shields.io/badge/-Development%20Package-red?style=for-the-badge&")
LOGO.append("logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlD")
LOGO.append("Q1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQ")
LOGO.append("XR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxN")
LOGO.append("AruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVS")
LOGO.append("PzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSw")
LOGO.append("gEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL")
LOGO.append("1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cna")
LOGO.append("te3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AA")
LOGO.append("AAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0")
LOGO.append("ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+Q")
LOGO.append("eJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAK")
LOGO.append("iMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOu")
LOGO.append("bQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/")
LOGO.append("bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfa")
LOGO.append("ut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/")
LOGO.append("lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAA")
LOGO.append("ABJRU5ErkJggg==)")

DEV_PACKAGE_LOGO = "".join(LOGO)

lines = []
with open("README.md", "r", encoding="utf-8") as desc_file:
    for line in desc_file:
        SRCH = "https://img.shields.io/pypi/status/crowdstrike-falconpy?label=package"
        REPL = "https://img.shields.io/pypi/status/crowdstrike-falconpy-dev?label=package"
        if SRCH in line:
            line = line.replace(SRCH, REPL)

        if "# FalconPy - The CrowdStrike Falcon SDK for Python" in line:
            new_line = f"{line}\n{DEV_PACKAGE_LOGO}\n\n"
            lines.append(new_line)
            lines.append("> This is the development package.")
            lines.append(" Please check https://pypi.org/project/crowdstrike-falconpy/")
            lines.append(" for the stable release.\n\n")
        else:
            lines.append(line)
LONG_DESCRIPTION = "".join(lines)
project_title = f"{_TITLE}-dev"

# Remove GitHub's emoji
emojis = [
    ":speech_balloon: ", ":bulb: ", ":pray: ", ":raised_hands: ", " :fire:", ":fire: ",
    "<small>", "</small>", " :mag_right:", " :dizzy:", " :memo:", " :coffee:", " :book:"
    ]
for emoji in emojis:
    LONG_DESCRIPTION = LONG_DESCRIPTION.replace(emoji, "")

LONG_DESCRIPTION = LONG_DESCRIPTION.replace("from falconpy import", "from falconpydev import")
LONG_DESCRIPTION = LONG_DESCRIPTION.replace("install crowdstrike-falconpy", "install crowdstrike-falconpy-dev")

setup(
    name=project_title,
    version=_VERSION,
    author=_AUTHOR,
    author_email=_AUTHOR_EMAIL,
    maintainer=_MAINTAINER,
    maintainer_email=_AUTHOR_EMAIL,
    docs_url=_DOCS_URL,
    description=_DESCRIPTION,
    keywords=_KEYWORDS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=_PROJECT_URL,
    project_urls={
        "Documentation": "https://www.falconpy.io",
        "Source": "https://github.com/CrowdStrike/falconpy/tree/dev/src/falconpy",
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
            "pydocstyle",
            "pylint",
            "pytest-cov",
            "pytest",
            "bandit",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Flake8",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
)
