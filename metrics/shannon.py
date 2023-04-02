#!/usr/bin/env python

from math import log2

def shannon_entropy(text):
    """Calculates the Shannon entropy of a given string."""
    # Count the frequency of each character in the string
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Calculate the entropy
    entropy = 0
    for count in freq.values():
        probability = count / len(text)
        entropy -= probability * log2(probability)
    
    return entropy