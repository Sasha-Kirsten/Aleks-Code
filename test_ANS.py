#!/usr/bin/env python

import sys
import unittest

sys.path.append("encodings")
from huffman import huffman_encoding
from ANS2 import encode

class TestEncoding(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_encoding(self):
        string: str = "zdvKvXBG"
        expect: str = "1011001101111010001000"
        output: str = encode(string)

        self.assertEqual(output, expect)

if __name__ == '__main__':
    unittest.main()
