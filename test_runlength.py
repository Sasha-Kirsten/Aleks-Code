#!/usr/bin/env python

import sys
import unittest

sys.path.append("encodings")
from runlength import run_length_encode

class TestEncoding(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_encoding(self):
        expected : list = [(1, 'z'), (1, 'd'), (1, 'v'), (1, 'K'), (1, 'v'), (1, 'X'), (1, 'B'), (1, 'G')]
        strInput : str = "zdvKvXBG"

        self.assertEqual(run_length_encode(strInput), expected)

if __name__ == '__main__':
    unittest.main()
