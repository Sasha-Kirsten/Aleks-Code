#!/usr/bin/env python

from pathlib    import Path
from utilities  import get_random_string
import sys

sys.path.append("metrics") #, "encodings")
sys.path.append("encodings")

from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
from shannon    import shannon_entropy as shannon
#from delta  import delta_encode as delta
from huffman    import huffman_encoding as huffman

csv_path = Path('huffman-tablesLettersNumbers500.csv')

with open(csv_path, mode="w") as file:

    file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, huffman_output_csv, huffman_kolmogorov,  huffman_shannon\n")

    for string_length in range(10, 500):
        test_str:str = get_random_string(length=string_length)
        test_string_kolmogorov: int = kolmogorov(test_str)
        test_string_shannon: float = shannon(test_str)

        huffman_encoded : str = (str(huffman(test_str)[0]))
        huffman_kolmogorov: int = kolmogorov(huffman_encoded)
        huffman_shannon: float = shannon(huffman_encoded)

        csv_template : str = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {huffman_encoded}, {huffman_kolmogorov}, {huffman_shannon}\n"

        print(f"Progress: {string_length} / 500")
        file.write(csv_template)