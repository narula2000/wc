from main import main


class TestMain:
    TEST_FILE = "test.txt"

    def test_newline_couts(self, capsys):
        """Testing the `-l` flag for the `wc` command"""
        test_args = ["-l", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert "7145 test.txt\n" == output

    def test_byte_counts(self, capsys):
        """Testing the `-c` flag for the `wc` command"""
        test_args = ["-c", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert "342190 test.txt\n" == output

    def test_word_counts(self, capsys):
        """Testing the `-w` flag for the `wc` command"""
        test_args = ["-w", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert "58164 test.txt\n" == output

    def test_char_counts(self, capsys):
        """Testing the `-m` flag for the `wc` command"""
        test_args = ["-m", self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert "339292 test.txt\n" == output

    def test_file_input(self, capsys):
        """Testing the file input for the `wc` command"""
        test_args = [self.TEST_FILE]
        main(test_args)
        output = capsys.readouterr().out
        assert "7145  58164  342190 test.txt\n" == output
