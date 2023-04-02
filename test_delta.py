#!/usr/bin/env python

import sys
import unittest

sys.path.append("encodings")
from delta import delta_encode

class TestEncoding(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_encoding(self):
        self.assertEqual(delta_encode("zdvKvXBG"), [122, -22, 18, -43, 43, -30, -22, 5])

if __name__ == '__main__':
    unittest.main()
