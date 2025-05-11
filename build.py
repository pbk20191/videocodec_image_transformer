from pathlib import Path
import sys
import subprocess
import argparse


def build(output_path: Path, entry: str):
    subprocess.run(
        [
            sys.executable,
            "-m", "shiv",
            # "-c", "entry",
            "-e", entry,
            "-o", str(output_path),
            "."
        ],
        check=True
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["cli", "gui"])
    parser.add_argument("output_path", type=Path)

    args = parser.parse_args()

    entrypoint = "entry.cli_entry:cli_main" if args.mode == "cli" else "entry.gui_entry:gui_main"
    build(args.output_path, entrypoint)