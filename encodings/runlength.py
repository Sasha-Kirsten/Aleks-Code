#!/usr/bin/env python

def run_length_encode(data):
    encoded = []
    i = 0
    while i < len(data):
        count = 1
        while i < len(data) - 1 and data[i] == data[i+1]:
            count += 1
            i += 1
        encoded.append((count, data[i]))
        i += 1
    return encoded