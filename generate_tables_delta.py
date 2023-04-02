#!/usr/bin/env python

from pathlib    import Path
from utilities  import get_random_string
import sys

sys.path.append("metrics") #, "encodings")
sys.path.append("encodings")

from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
from shannon    import shannon_entropy as shannon
from delta  import delta_encode as delta
from huffman    import huffman_encoding as huffman

csv_path = Path('delta-tablesLettersNumbers500.csv')


with open(csv_path, mode="w") as file:

    file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, delta_output_csv, delta_huffman_encoded, delta_kolmogorov,  delta_shannon\n")
    for string_length in range(10, 500):

        test_str:str = get_random_string(length=string_length)
        test_string_kolmogorov: int = kolmogorov(test_str)
        test_string_shannon: float = shannon(test_str)
        delta_output: list = delta(test_str)

        delta_output_csv: str = ""

        for tuple_item in delta_output:
            delta_output_csv += str(tuple_item) + " "

        delta_huffman_encoded : str = huffman(str(delta_output_csv))[0]
        delta_kolmogorov: int = kolmogorov(delta_huffman_encoded)
        delta_shannon: float = shannon(delta_huffman_encoded)

        csv_template : str = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {delta_output_csv}, {delta_huffman_encoded}, {delta_kolmogorov}, {delta_shannon}\n"

        print(f"Progress: {string_length} / 500")
        file.write(csv_template)

