#!python

from finder import find, find_index, find_all_indexes
import unittest

# find(string, pattern) -> true if string contains pattern
# find_index(string, pattern) -> starting index of first occurence
# find_all_indexes(string, pattern) -> list all indexes with occurence
class TestFinder(unittest.TestCase):

    def test_find_with_none_string(self):
        string = None
        pattern = 'one'
        assert find(string, pattern) is False

    def test_find_with_empty_string(self):
        string = ''
        pattern = 'one'
        assert find(string, pattern) is False

    def test_find_with_none_pattern(self):
        string = ''
        pattern = None
        assert find(string, pattern) is False

    def DISABLED_test_find_with_empty_pattern(self):
        string = ''
        pattern = ''
        assert find(string, pattern) is True
        string = 'a'
        pattern = ''
        assert find(string, pattern) is False

    def test_find_with_letter_pattern_in_string(self):
        string = 'onetwothreefourfive'
        assert find(string, 'one') is True
        assert find(string, 'two') is True
        assert find(string, 'three') is True
        assert find(string, 'four') is True
        assert find(string, 'five') is True

    def test_find_with_leter_pattern_not_in_string(self):
        string = 'onetwothreefourfive'
        assert find(string, 'six') is False
        assert find(string, 'seven') is False

    def test_find_with_number_pattern_in_string(self):
        string = '12345'
        assert find(string, '1') is True
        assert find(string, '12') is True
        assert find(string, '123') is True
        assert find(string, '1234') is True
        assert find(string, '12345') is True

    def test_find_with_number_pattern_not_in_string(self):
        string = '12345'
        assert find(string, '6') is False
        assert find(string, '67') is False

    def test_find_with_any_pattern_in_string(self):
        string = 'asdn\y of23h01148n+)&^%#@xc'
        assert find(string, '8n+)&') is True
        assert find(string, '8n+)&A') is False
        assert find(string, 'A8n+)&') is False
        assert find(string, '\y ') is True


if __name__ == '__main__':
    unittest.main()
