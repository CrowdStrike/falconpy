import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="falconpy", # Replace with your own username
    version="0.1.7",
    author="CrowdStrike",
    maintainer="Joshua Hiller",
    description="The CrowdStrike Falcon API SDK for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CrowdStrike/falconpy",
    packages=setuptools.find_packages(),
    package_dir={'': 'falconpy'},
    install_requires=[
	"requests",
	"urllib3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
