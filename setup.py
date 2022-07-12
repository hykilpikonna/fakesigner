#!/usr/bin/env python3
import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent.absolute()

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='fakesigner',
    version='1.0.0',
    description="iOS IPA File Fake-Signer Script",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hykilpikonna/fakesigner-ios",
    author="Azalea Gui",
    author_email="me@hydev.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: iOS"
    ],
    scripts=['pypi/fakesigner']
)