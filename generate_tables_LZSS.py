#!/usr/bin/env python

from pathlib    import Path
from utilities  import get_random_string
import sys

sys.path.append("metrics") #, "encodings")
sys.path.append("encodings")

from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
from shannon    import shannon_entropy as shannon
from lzss import encoding

csv_path = Path('LZSS-tablesLettersNumbers500.csv')


with open(csv_path, mode="w") as file:

    file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, LZSS_output_csv, LZSS_kolmogorov, LZSS_shannon\n")

    for string_length in range(10, 500):
        test_str:str = get_random_string(length=string_length)
        test_string_kolmogorov: int = kolmogorov(test_str)
        test_string_shannon: float = shannon(test_str)
        LZSS_output: list = encoding(test_str)

        LZSS_output_csv: str = ""

        for tuple_item in LZSS_output:
            LZSS_output_csv += str(tuple_item) + " "

        LZSS_kolmogorov: int = kolmogorov(LZSS_output_csv)
        LZSS_shannon: float = shannon(LZSS_output_csv)

        csv_template : str = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {LZSS_output_csv}, {LZSS_kolmogorov}, {LZSS_shannon}\n"

        print(f"Progress: {string_length} / 500")
        file.write(csv_template)