from argparse import ArgumentParser

def init_argparse() -> ArgumentParser:
    parser = ArgumentParser(
        usage="%(prg)s [OPTION] [FILE]...",
        description="Produce a text file of lines sorted from another text file"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("filepath")
    return parser

def sort_list(filepath) -> None:
    f = open(filepath, 'r')
    l = f.readlines()
    l = list(map(lambda x: x.strip(), l))
    l.sort()
    for e in l:
        print(e)

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    sort_list(args.filepath)

if __name__ == '__main__':
    main()
