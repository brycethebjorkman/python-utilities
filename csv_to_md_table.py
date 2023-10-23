from argparse import ArgumentParser
import csv
import os

def init_argparse() -> ArgumentParser:
    parser = ArgumentParser(
        usage="%(prg)s [OPTION] [FILE(s)]...",
        description="convert CSV files to MD tables"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("files", nargs="*")
    return parser

def csv_to_md_table(file):
    with open(file, "r") as f:
        r = csv.reader(f)
        for row in r:
            s = "|"
            for col in row:
                s += " " + col + " |"
            print(s)

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    for file in args.files:
        try:
            md = csv_to_md_table(file)
            print(md)
            continue
        except (FileNotFoundError, IsADirectoryError, IOError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
