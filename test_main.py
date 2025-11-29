import io
import sys

from main import main


class TestFileInput:
    TEST_FILE = "test.txt"

    def test_newline_couts(self, capsys):
        """Testing the `-l` flag for the `wc` command"""
        test_args = ["-l", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert output == "7145 test.txt\n"

    def test_byte_counts(self, capsys):
        """Testing the `-c` flag for the `wc` command"""
        test_args = ["-c", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert output == "342190 test.txt\n"

    def test_word_counts(self, capsys):
        """Testing the `-w` flag for the `wc` command"""
        test_args = ["-w", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert output == "58164 test.txt\n"

    def test_char_counts(self, capsys):
        """Testing the `-m` flag for the `wc` command"""
        test_args = ["-m", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert output == "339292 test.txt\n"

    def test_file_input(self, capsys):
        """Testing the file input for the `wc` command"""
        test_args = [self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert output == "7145  58164  342190 test.txt\n"

    def test_multiple_file_input(self, capsys):
        """Testing multiple file inputs for the `wc` command"""
        test_args = [self.TEST_FILE, self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        expected = "7145  58164  342190 test.txt\n7145  58164  342190 test.txt\n14290  116328  684380 total\n"
        assert expected == output


class TestSTDInput:
    TEST_INPUT = b"hello\nworld\n"

    def test_stdin_line_count(self, capsys):
        """Testing the piped stdin input in `-l` flag the `wc` command"""
        sys.stdin = io.TextIOWrapper(io.BytesIO(self.TEST_INPUT))

        main(["-l"])
        output = capsys.readouterr().out

        assert output == "2 \n"

    def test_stdin_byte_count(self, capsys):
        """Testing the piped stdin input in `-c` flag the `wc` command"""
        sys.stdin = io.TextIOWrapper(io.BytesIO(self.TEST_INPUT))

        main(["-c"])
        output = capsys.readouterr().out

        assert output == "12 \n"

    def test_stdin_word_count(self, capsys):
        """Testing the piped stdin input in `-w` flag the `wc` command"""
        sys.stdin = io.TextIOWrapper(io.BytesIO(self.TEST_INPUT))

        main(["-w"])
        output = capsys.readouterr().out

        assert output == "2 \n"

    def test_stdin_char_count(self, capsys):
        """Testing the piped stdin input in `-m` flag the `wc` command"""
        sys.stdin = io.TextIOWrapper(io.BytesIO(self.TEST_INPUT))

        main(["-m"])
        output = capsys.readouterr().out

        assert output == "12 \n"

    def test_stdin_total_count(self, capsys):
        """Testing the piped stdin input in `-m` flag the `wc` command"""
        sys.stdin = io.TextIOWrapper(io.BytesIO(self.TEST_INPUT))

        main([])
        output = capsys.readouterr().out

        assert output == "2  2  12 \n"
