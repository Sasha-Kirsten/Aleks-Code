#!/usr/bin/env python

from random import choice
from string import ascii_letters, digits, punctuation

binary_code = "01"

def get_random_string(length):
	#with the combination of lower and upper case
	result_str = ''.join(choice(ascii_letters + digits) for i in range(length))
	#print random string
	return result_str