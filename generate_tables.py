#!/usr/bin/env python

from pathlib    import Path
from utilities  import get_random_string
import sys

sys.path.append("metrics") #, "encodings")
sys.path.append("encodings")

from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
from shannon    import shannon_entropy as shannon
from runlength  import run_length_encode as runlength
from huffman    import huffman_encoding as huffman

csv_path = Path('runlength-tablesLettersNumbers500.csv')



with open(csv_path, mode="w") as file:

    file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, runlength_output_csv, runlength_huffman_encoded, runlength_kolmogorov,  runlength_shannon\n")

    for string_length in range(10, 500):
        test_str:str = get_random_string(length=string_length)
        #string_length : str = len(test_str)
        test_string_kolmogorov: int = kolmogorov(test_str)
        test_string_shannon: float = shannon(test_str)
        runlength_output: list = runlength(test_str)

        runlength_output_csv: str = ""

        for tuple_items in runlength_output:
            for tuple_item in tuple_items:
                runlength_output_csv += str(tuple_item) + ""
            runlength_output_csv += ""

        runlength_huffman_encoded : str = huffman(str(runlength_output_csv))[0]
        runlength_kolmogorov: int = kolmogorov(runlength_huffman_encoded)
        runlength_shannon: float = shannon(runlength_huffman_encoded)

        csv_template : str = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {runlength_output_csv}, {runlength_huffman_encoded}, {runlength_kolmogorov}, { runlength_shannon}\n"

        print(f"Progress: {string_length} / 500")
        file.write(csv_template)





    
