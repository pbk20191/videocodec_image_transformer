import PIL
from PIL import Image

from pathlib import Path
from typing import Optional, Union
import os
import shutil
from enum import Enum
import click
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp", ".heic", ".heif"}

SUPPORTED_FORMATS = {"heif", "avif"}


class ImageFormat(str,Enum):
    HEIF = "heif"
    AVIF = "avif"

def convert_image(input_path:Path, output_path:Path, format:ImageFormat, quality:int | None = None) -> None:
    """
    Convert an image to HEIF or AVIF format and save it to the specified output path.
    
    Args:
        inputPath (Path): Path to the input image file.
        outputPath (Path): Path to save the converted image.
        format (ImageFormat): The desired output format (HEIF or AVIF).
    """
    Image.init()
    import pillow_heif
    pillow_heif.register_heif_opener()
    import pillow_avif
    dest_suffix = ".heif" if format == ImageFormat.HEIF else ".avif"
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
                        dest_file = dest_root / (Path(file).stem + dest_suffix)
                        if format == ImageFormat.HEIF:
                            img.save(dest_file, format=format.value.upper(), quality=quality)
                        else:
                            if quality is None:
                                img.save(dest_file, format=format.value.upper())
                            else:
                                img.save(dest_file, format=format.value.upper(), quality=quality)
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