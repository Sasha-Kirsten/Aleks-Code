#!/usr/bin/env python

import sys
import unittest

sys.path.append("encodings")
from lzss import encoding

class TestEncoding(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_encoding(self):
        string: str = "zdvKvXBG"
        expect: list = [122, 100, 118, 75, 118, 88, 66, 71]
        output: str = encoding(string)

        self.assertEqual(output, expect)

if __name__ == '__main__':
    unittest.main()