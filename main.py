import argparse


def setup_parser(arguments=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-c", "--bytes", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-m", "--chars", action="store_true")
    parser.add_argument("file", nargs="?")  # optional file argument
    return parser.parse_args(arguments)


def count_lines(file):
    with open(file, "r") as txt:
        lines = txt.readlines()

    return sum((1 for line in lines))


def flag_hanlder(arguments):
    if arguments.lines:
        line_count = count_lines(arguments.file)
        print(f"{line_count} {arguments.file}")
    elif arguments.bytes:
        print("Byte count detected")
    elif arguments.words:
        print("Word count detected")
    elif arguments.chars:
        print("Char count detected")
    else:
        print("No flag")


def main(argv=None):
    arguments = setup_parser(argv)
    flag_hanlder(arguments)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
