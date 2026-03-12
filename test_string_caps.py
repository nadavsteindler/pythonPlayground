import pytest
from string_caps import capitalize


class TestCapitalize:
    def test_empty_string(self):
        assert capitalize("") == ""

    def test_single_character(self):
        assert capitalize("a") == "a"

    def test_two_character_word(self):
        assert capitalize("ab") == "aB"

    def test_one_word(self):
        assert capitalize("hello") == "hEllo"

    def test_two_words(self):
        assert capitalize("hello world") == "hEllo wOrld"

    def test_short_words(self):
        assert capitalize("i a") == "i a"

    def test_long_word(self):
        assert capitalize("abcdefghijklmnop") == "aBcdefghijklmnop"

    def test_multiple_spaces(self):
        assert capitalize("a  b") == "a  b"

    def test_leading_space(self):
        assert capitalize(" hello") == " hEllo"

    def test_trailing_space(self):
        assert capitalize("hello ") == "hEllo "

    def test_already_uppercase(self):
        assert capitalize("HELLO") == "HELLO"

    def test_second_letter_already_caps(self):
        assert capitalize("hEllo") == "hEllo"

    def test_many_words(self):
        assert capitalize("the quick brown fox") == "tHe qUick bRown fOx"
