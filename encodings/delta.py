#!/usr/bin/env python

def delta_encode(data):
    if len(data) == 0:
        return []

    result = [ord(data[0])]
    for i in range(1, len(data)):
        diff = ord(data[i]) - ord(data[i-1])
        result.append(diff)
        
    return result