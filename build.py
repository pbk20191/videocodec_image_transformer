from pathlib import Path
import sys
import subprocess

def build_gui(output_path:Path):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "shiv",
            "-c",
            "hello",
            "-e",
            "hello:gui_main",
            "-o",
            str(output_path),
            "."
        ],
        check=True
    )

def build_cli(output_path:Path):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "shiv",
            "-c",
            "hello",
            "-o",
            str(output_path),
            "."
        ],
        check=True
    )


