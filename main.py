import argparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-c", "--bytes", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-m", "--chars", action="store_true")
    parser.add_argument("file", nargs="?")  # optional file argument
    args = parser.parse_args(argv)

    if args.lines:
        print("List flag detected")
    elif args.bytes:
        print("Byte count detected")
    elif args.words:
        print("Word count detected")
    elif args.chars:
        print("Char count detected")
    else:
        print("No flag")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
