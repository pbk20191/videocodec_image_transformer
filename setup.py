from setuptools import setup, find_packages
from pathlib import Path
import os
import shutil
import sys
import subprocess


setup(
    name="image-to-heif-avif",
    version="0.1.0",
    author="pbk20191",
    author_email="impbk2002@gmail.com",
    description="A simple image converter for HEIF and AVIF formats.",
    long_description_content_type="text/markdown",
    py_modules=["hello",],
    requires=["pillow", "pillow_heif", "click"],
    install_requires=[
        "pillow>=8.0.0",
        "pillow_heif>=0.1.0",
        "click>=7.0",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hello=hello:cli_main",
        ],
        "gui_scripts": [
            "hello=hello:gui_main",
        ],
    },
)