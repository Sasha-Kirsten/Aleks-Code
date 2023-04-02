import heapq
import struct

# Step 1: Count the frequency of each symbol in the input data.
def count_freqs(data):
    freqs = [0] * len(data)
    for byte in range(len(data)):
        freqs[byte] += 1
    print(freqs)
    return freqs

# Step 2: Normalize the frequencies so they sum up to 2^tableLog.
def normalize_freqs(freqs, tableLog):
    max_freq = max(freqs)
    if max_freq == 0:
        return [0] * len(freqs)
    scale = ((1 << tableLog) - len(freqs)) // max_freq
    table = [0] * tableLog
    for i in range(len(freqs)):
        if freqs[i] > 0:
            table[i] = (freqs[i] * scale + (1 << (tableLog - 1))) // (1 << tableLog)
    print(table)
    return table

# Step 3: Build a Huffman tree using the normalized frequencies.
def build_huffman_tree(freqs):
    heap = []
    for i in range(len(freqs)):
        if freqs[i] > 0:
            heapq.heappush(heap, (freqs[i], i))
    while len(heap) > 1:
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, (node1, node2)))
    return heap[0][1]

# Step 4: Generate a prefix code from the Huffman tree.
def generate_prefix_code(tree):
    code_lengths = [0] * 256
    assign_code_lengths(tree, code_lengths, 0)
    prefix_code = [0] * 256
    assign_prefix_codes(tree, prefix_code, 0, code_lengths)
    return code_lengths, prefix_code

def assign_code_lengths(node, code_lengths, length):
    if isinstance(node, int):
        code_lengths[node] = length
    else:
        assign_code_lengths(node[0], code_lengths, length + 1)
        assign_code_lengths(node[1], code_lengths, length + 1)

def assign_prefix_codes(node, prefix_code, code, code_lengths):
    if isinstance(node, int):
        prefix_code[node] = code
    else:
        assign_prefix_codes(node[0], prefix_code, code << 1, code_lengths)
        assign_prefix_codes(node[1], prefix_code, (code << 1) | 1, code_lengths)

# Step 5: Build a decoding table from the prefix code.
def build_decoding_table(code_lengths, prefix_code, table_log):
    table_size = 1 << table_log
    table_mask = table_size - 1
    table = [0] * table_size
    min_code = [table_size] * (table_log+1)
    max_code = [0] * (table_log+1)
    for symbol in range(len(code_lengths)):
        if code_lengths[symbol] == 0:
            continue
        if code_lengths[symbol] > table_log:
            raise ValueError("Code for symbol {} is too long".format(symbol))
        code = prefix_code[symbol]
        bits_to_fill = table_log - code_lengths[symbol]
        for i in range(1 << bits_to_fill):
            index = (code << bits_to_fill) | i
            table[index] = symbol
            if code < min_code[code_lengths[symbol]]:
                min_code[code_lengths[symbol]] = code
            if code > max_code[code_lengths[symbol]]:
                max_code[code_lengths[symbol]] = code
    return table, min_code, max_code, table_mask


# Step 6: Compress the input data using the prefix code and decoding table.
def compress_data(data, code_lengths, prefix_code, table_log, decoding_table):
    bits = []
    bits_append = bits.append
    code = 0
    length = 0
    for byte in range(len(data)-1):
        bits_append(prefix_code[byte])
        bits_append(prefix_code[len(data)])
    while bits:
        code_lengths = bits.pop(0)
        code = ((code << code_lengths) | bits.pop(0)) & decoding_table[code_lengths]
        length += code_lengths
    while length > 8:
        length -= 8
        yield(code >> length) & 0xff 


# Step 7: Decompress the input data using the decoding table.
def decompress_data(data, code_lengths, prefix_code, table_log, decoding_table):
    bits = []
    bits_append = bits.append
    code = 0
    length = 0
    for byte in data:
        code = ((code << 8) | byte) & decoding_table[table_log]
        length += 8
        while length >= table_log:
            length -= table_log
            bits_append(code >> length)
    print("bits: ", bits)
    while bits:
        if len(bits) > 0 :
            code = bits.pop(0)
            len_code = code_lengths[code]
            code = ((code << len_code) | bits.pop(0)) & decoding_table[len_code]
            length += len_code
            while length >= 8:
                length -= 8
                yield (code >> length) & 0xff
                code = ((code << 8) | bits.pop(0)) & decoding_table[table_log]