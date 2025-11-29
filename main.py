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


def count_lines(bytes):
    lines = 0
    for char in bytes.decode():
        if char == "\n":
            lines += 1
    return lines


def count_byte(bytes):
    return len(bytes)


def count_words(bytes):
    words = bytes.decode().split()
    return len([word for word in words if words != ""])


def count_chars(bytes):
    content = bytes.decode()
    return len(content)


def handle_file(arguments, bytes, agg, filename):
    if arguments.lines:  # -l
        line_count = count_lines(bytes)
        agg.line_count += line_count
        print(f"{line_count} {filename}")
    elif arguments.bytes:  # -c
        byte_count = count_byte(bytes)
        agg.byte_count += byte_count
        print(f"{byte_count} {filename}")
    elif arguments.words:  # -w
        word_count = count_words(bytes)
        agg.word_count += word_count
        print(f"{word_count} {filename}")
    elif arguments.chars:  # -m
        char_count = count_chars(bytes)
        print(f"{char_count} {filename}")
    else:  # We will use flag -c, -l -w
        line_count = count_lines(bytes)
        word_count = count_words(bytes)
        byte_count = count_byte(bytes)
        agg.line_count += line_count
        agg.byte_count += byte_count
        agg.word_count += word_count
        print(f"{line_count}  {word_count}  {byte_count} {filename}")


def flag_hanlder(arguments, agg):
    if arguments.files:
        for file in arguments.files:
            if os.path.isfile(file):
                with open(file, "rb") as bytes:
                    handle_file(arguments, bytes.read(), agg, file)
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
        handle_file(arguments, sys.stdin.buffer.read(), agg, "")


def main(argv=None):
    arguments = setup_parser(argv)
    agg = Aggregator()
    flag_hanlder(arguments, agg)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
