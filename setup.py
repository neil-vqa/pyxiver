import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Details
NAME = "pyxiver"
VERSION = "1.0.1"
DESCRIPTION = "Python wrapper for the arXiv.org public API."
URL = "https://github.com/neil-vqa/pyxiver"
AUTHOR = "Neil Van Alino"
EMAIL = "nvq.alino@gmail.com"
REQUIRED = [
    "requests", "xmltodict"
]


# This call to setup() does all the work
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=REQUIRED,
)
