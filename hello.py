import PIL
from PIL import Image
import pillow_heif
from pathlib import Path
from typing import Optional, Union
import os
import shutil
from enum import Enum
import click

SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}

SUPPORTED_FORMATS = {"heif", "avif"}


class ImageFormat(str,Enum):
    HEIF = "heif"
    AVIF = "avif"

def convert_image(input_path:Path, output_path:Path, format:ImageFormat) -> None:
    """
    Convert an image to HEIF or AVIF format and save it to the specified output path.
    
    Args:
        inputPath (Path): Path to the input image file.
        outputPath (Path): Path to save the converted image.
        format (ImageFormat): The desired output format (HEIF or AVIF).
    """
    pillow_heif.register_heif_opener()
    for root, _, files in os.walk(input_path):
        rel_root = Path(root).relative_to(input_path)
        dest_root = output_path / rel_root
        dest_root.mkdir(parents=True, exist_ok=True)

        for file in files:
            ext = Path(file).suffix.lower()
            src_file = Path(root) / file

            if ext in SUPPORTED_EXTS:
                try:
                    with Image.open(src_file) as img:
                        dest_suffix = ".heif" if format == ImageFormat.HEIF else ".avif"
                        dest_file = dest_root / (Path(file).stem + dest_suffix)
                        img.save(dest_file, format=format.name.upper(), quality=None)
                        click.echo(f"[✓] {format.name.upper()}: {src_file} → {dest_file}")
                except Exception as e:
                    click.echo(f"[!] Failed to convert {src_file}: {e}", err=True)
            else:
                shutil.copy2(src_file, dest_root / file)
                click.echo(f"[=] Copied: {src_file}")


import os
import shutil
from pathlib import Path

from PIL import Image
import click



@click.command()
@click.argument("input_path", type=click.Path(exists=True, file_okay=False))
@click.argument("output_path", type=click.Path())
@click.option("--format", "out_format", type=click.Choice(SUPPORTED_FORMATS), default="heif", help="Output format: heif or avif")
def cli_main(input_path, output_path, out_format):
    """
    Convert images under INPUT_PATH to HEIF or AVIF format and write them into OUTPUT_PATH.
    Folder structure is preserved.
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    convert_image(input_path, output_path, ImageFormat.HEIF if out_format == "heif" else ImageFormat.AVIF)


import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path

class ImageConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter (HEIF / AVIF)")
        self.geometry("500x300")
        self.resizable(True, True)

        # Input folder
        self.input_path_var = tk.StringVar()
        self.output_path_var = tk.StringVar()
        self.format_var = tk.StringVar(value=ImageFormat.HEIF.value)

        ttk.Label(self, text="Input Folder:").pack(anchor='w', padx=10, pady=(15, 0))
        ttk.Entry(self, textvariable=self.input_path_var, width=60).pack(padx=10)
        ttk.Button(self, text="Browse", command=self.browse_input).pack(pady=5)

        ttk.Label(self, text="Output Folder:").pack(anchor='w', padx=10)
        ttk.Entry(self, textvariable=self.output_path_var, width=60).pack(padx=10)
        ttk.Button(self, text="Browse", command=self.browse_output).pack(pady=5)

        ttk.Label(self, text="Format:").pack(anchor='w', padx=10)
        ttk.Combobox(self, textvariable=self.format_var, values=[f.value for f in ImageFormat]).pack(padx=10, pady=5)
        ttk.Button(self, text="Convert", command=self.run_conversion).pack(pady=10)


    def browse_input(self):
        path = filedialog.askdirectory(title="Select Input Directory")
        if path:
            self.input_path_var.set(path)

    def browse_output(self):
        path = filedialog.askdirectory(title="Select Output Directory")
        if path:
            self.output_path_var.set(path)

    def run_conversion(self):
        input_path = Path(self.input_path_var.get())
        output_path = Path(self.output_path_var.get())
        format_str = self.format_var.get()

        if not input_path.exists() or not output_path.exists():
            messagebox.showerror("Error", "Both input and output directories must exist.")
            return

        try:
            convert_image(input_path, output_path, ImageFormat(format_str))
            messagebox.showinfo("Success", f"Images converted to {format_str.upper()} successfully.")
            # self.quit()
        except Exception as e:
            messagebox.showerror("Conversion Error", str(e))

def gui_main():
    app = ImageConverterGUI()
    app.mainloop()


