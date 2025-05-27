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
    py_modules=["entry",],
    requires=["Pillow", "pillow_heif", "click", "pillow_avif_plugin"],
    install_requires=[
        "Pillow>=8.0.0",
        "pillow_heif>=0.1.0",
        "click>=7.0",
        "pillow_avif_plugin>=1.5.2",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "entry=entry.cli_entry:cli_main",
        ],
        "gui_scripts": [
            "entry=entry.gui_entry:gui_main",
        ],
    },
)
