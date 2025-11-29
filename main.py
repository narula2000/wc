import argparse
import os


def setup_parser(arguments=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-c", "--bytes", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-m", "--chars", action="store_true")
    parser.add_argument("file", nargs="?")  # optional file argument
    return parser.parse_args(arguments)


def read_file(file):
    with open(file, "r") as txt:
        lines = txt.readlines()
    return lines


def count_lines(file):
    lines = read_file(file)
    return sum((1 for line in lines))


def count_byte(file):
    with open(file, "rb") as txt:
        content = txt.read()
    return len(content)


def count_words(file):
    lines = read_file(file)
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
    return word_count


def count_chars(file):
    with open(file, "rb") as txt:
        content = txt.read().decode()
    return len(content)


def flag_hanlder(arguments):
    if not arguments.file or not os.path.isfile(arguments.file):
        print("A file is needed")
        return

    if arguments.lines:  # -l
        line_count = count_lines(arguments.file)
        print(f"{line_count} {arguments.file}")
    elif arguments.bytes:  # -c
        byte_count = count_byte(arguments.file)
        print(f"{byte_count} {arguments.file}")
    elif arguments.words:  # -w
        word_count = count_words(arguments.file)
        print(f"{word_count} {arguments.file}")
    elif arguments.chars:  # -m
        char_count = count_chars(arguments.file)
        print(f"{char_count} {arguments.file}")
    else:  # We will use flag -c, -l -w
        line_count = count_lines(arguments.file)
        word_count = count_words(arguments.file)
        byte_count = count_byte(arguments.file)
        print(f"{line_count}  {word_count}  {byte_count} {arguments.file}")


def main(argv=None):
    arguments = setup_parser(argv)
    flag_hanlder(arguments)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
