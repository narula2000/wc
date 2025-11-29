import argparse
import os
import sys

from dataclasses import dataclass


@dataclass
class Aggregator:
    line_count: int = 0
    word_count: int = 0
    byte_count: int = 0


def setup_parser(arguments=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-c", "--bytes", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-m", "--chars", action="store_true")
    parser.add_argument("files", metavar="FILE", default="", type=str, nargs="*")
    return parser.parse_args(arguments)


def read_file(file):
    with open(file, "r") as txt:
        lines = txt.readlines()
    return lines


def count_lines(file):
    lines = read_file(file)
    return sum((1 for _ in lines))


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


def handle_file(arguments, file, agg):
    if arguments.lines:  # -l
        line_count = count_lines(file)
        agg.line_count += line_count
        print(f"{line_count} {file}")
    elif arguments.bytes:  # -c
        byte_count = count_byte(file)
        agg.byte_count += byte_count
        print(f"{byte_count} {file}")
    elif arguments.words:  # -w
        word_count = count_words(file)
        agg.word_count += word_count
        print(f"{word_count} {file}")
    elif arguments.chars:  # -m
        char_count = count_chars(file)
        print(f"{char_count} {file}")
    else:  # We will use flag -c, -l -w
        line_count = count_lines(file)
        word_count = count_words(file)
        byte_count = count_byte(file)
        agg.line_count += line_count
        agg.byte_count += byte_count
        agg.word_count += word_count
        print(f"{line_count}  {word_count}  {byte_count} {file}")


def flag_hanlder(arguments, agg):
    if arguments.files:
        for file in arguments.files:
            if os.path.isfile(file):
                handle_file(arguments, file, agg)
        if len(arguments.files) > 1:
            if arguments.lines:  # -l
                print(f"{agg.line_count} total")
            elif arguments.bytes:  # -c
                print(f"{agg.byte_count} total")
            elif arguments.words:  # -w
                print(f"{agg.word_count} total")
            else:
                print(f"{agg.line_count}  {agg.word_count}  {agg.byte_count} total")
    else:
        handle_file(arguments, sys.stdin.buffer.read(), agg)


def main(argv=None):
    arguments = setup_parser(argv)
    agg = Aggregator()
    flag_hanlder(arguments, agg)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
