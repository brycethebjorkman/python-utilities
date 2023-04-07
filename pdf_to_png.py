from argparse import ArgumentParser
import fitz #package PyMuPDF on [PyPi](https://pypi.org/project/PyMuPDF/)

def init_argparse() -> ArgumentParser:
    parser = ArgumentParser(
        usage="%(prg)s [OPTION] [FILE]...",
        description="Convert a PDF file to a PNG file"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("-d", "--dpi", type=int)
    parser.add_argument("files", nargs="*")
    return parser

def pdf_to_png(file, dpi) -> fitz.Pixmap:
    doc = fitz.open(file)
    pix_list = []
    for page in doc:
        pix_list.append(page.get_pixmap(dpi=dpi))
    x0, y0, x1, y1 = [0, 0, 0, 0]
    for pix in pix_list:
        x1 = max(x1, pix.width)
        y1 += pix.height + dpi
    result = fitz.Pixmap(fitz.Colorspace(fitz.CS_RGB), fitz.IRect(x0, y0, x1, y1))
    height_covered = 0
    for pix in pix_list:
        for y in range(pix.height):
            for x in range(pix.width):
                result.set_pixel(x, y + height_covered, pix.pixel(x, y))
        height_covered += pix.height + dpi
    return result

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    for file in args.files:
        try:
            png = pdf_to_png(file, args.dpi)
            png.save(file + ".png", output="png")
            continue
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
