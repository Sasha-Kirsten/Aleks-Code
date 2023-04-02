#!/usr/bin/env python

class Node_2:
    def __init__(self,data):
        self.data = data
        self.children = {}

def estimate_kolmogorov_complexity(string):
    root = Node_2('')
    node_count = 1
    for i in range(len(string)):
        node = root
        for j in range(i, len(string)):
            char = string[j]
            if char not in node.children:
                node.children[char] = Node_2(char)
                node_count += 1
            node = node.children[char]
    return node_count 