
import click
from pathlib import Path
from imgconv.comon_img import convert_image, ImageFormat, SUPPORTED_FORMATS


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


if __name__ == "__main__":
    cli_main()