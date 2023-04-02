#!/usr/bin/env python

class Node:
    def __init__(self, probability, symbol, left = None, right = None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

the_code = dict()

def CalculateCode(node, value=''):
    #a huffman code for current node
    newValue = value + str(node.code)

    if(node.left):
        CalculateCode(node.left,newValue)
    if(node.right):
        CalculateCode(node.right, newValue)

    if(not node.left and not node.right):
        the_code[node.symbol] = newValue

    return the_code

def CalculateProbabilityofSymbols(the_data):
    the_symbols = dict()

    for item in the_data:
        if the_symbols.get(item) == None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols

def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])


    return the_string


def TotalGain(the_data,coding):
    #total bit space to store the data before compression
    beforeCompression = len(the_data)*8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        #calculate how many bit is required for the symbol
        afterCompression += the_count *  len(coding[symbol])

def huffman_encoding(the_data):
    assert len(the_data) > 0, "The input data is empty"

    symbolWithProbs = CalculateProbabilityofSymbols(the_data)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()

    the_nodes = []

    #converting symbols and probabilites into Huffman tree nodes
    for symbol in the_symbols:
        the_nodes.append(Node(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        #sorting all the nodes in ascending order based on t
        the_nodes = sorted(the_nodes, key= lambda x: x.probability)

        #pickingtwo smallest nodes
        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        #combining the 2 smallest nodes to create new nod
        newNode = Node(left.probability + right.probability, left.symbol+right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)
        
    HuffmanEncoding = CalculateCode(the_nodes[0])
    TotalGain(the_data, HuffmanEncoding)
    encoded_output = OutputEncoded(the_data, HuffmanEncoding)
    return encoded_output, the_nodes[0]