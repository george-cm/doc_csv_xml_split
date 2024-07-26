"""Save XML strings from a csv file into individual XML files."""

import argparse
import csv
import ctypes
from pathlib import Path
from typing import Any
from typing import Union


def main() -> None:
    """Main function."""

    args: argparse.Namespace = parse_args()

    input_file = Path(args.input_file)
    if not input_file.exists():
        raise FileNotFoundError(f"Input file {input_file} not found.")
    if not input_file.is_file():
        raise NotADirectoryError(f"Input file {input_file} is not a file.")

    xml_string_column: str = "Data"
    split_xml_file(input_file, xml_string_column)


def split_xml_file(input_file: Path, xml_string_column: str = "Data") -> None:
    """Extract the XML strings into individual XML files from the csv input file."""
    csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))
    with input_file.open("r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader, start=1):
            print(f"Processing row {i}...")
            xml_string: Union[str, Any] = row[xml_string_column]
            xml_file: Path = input_file.parent / f"{input_file.stem}_{i}.xml"
            with xml_file.open("w", newline="") as outf:
                outf.write(xml_string)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to input file.")
    return parser.parse_args()


if __name__ == "__main__":
    main()
