import argparse
import fitz #package PyMuPDF on [PyPi](https://pypi.org/project/PyMuPDF/)

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prg)s [OPTION] [FILE]...",
        description="Rotate the pages of a PDF file"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("-r", "--rotation", type=int, choices=[90, 180, 270])
    parser.add_argument("files", nargs="*")
    return parser

def rotate_pdf_pages(file, rotation):
    doc = fitz.open(file)
    for page in doc:
        page.set_rotation(rotation)
    doc.saveIncr()

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    for file in args.files:
        try:
            png = rotate_pdf_pages(file, args.rotation)
            continue
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()

