# #!/usr/bin/env python

# from pathlib    import Path
# from utilities  import get_random_string
# import sys

# sys.path.append("metrics") #, "encodings")
# sys.path.append("encodings")

# from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
# from shannon    import shannon_entropy as shannon
# # from ANS3  import ANSEncoder as ANSEncoder
# # from ANS3 import encode as encode




# import sys
# from collections import defaultdict

# class ANSEncoder:
#     def __init__(self, message):
#         self.message = message
#         self.frequencies = defaultdict(int)
#         for symbol in message:
#             self.frequencies[symbol] += 1
#         self.cumulative_frequencies = {}
#         self.total_count = sum(self.frequencies.values())
#         self.build_cumulative_frequencies()
    
#     # def build_cumulative_frequencies(self):
#     #     self.cumulative_frequencies[0] = 0
#     #     for symbol, count in sorted(self.frequencies.items()):
#     #         self.cumulative_frequencies[symbol] = self.cumulative_frequencies.get(symbol - 1, 0) + count

#     def build_cumulative_frequencies(self):
#         sorted_symbols = sorted(self.frequencies.keys())
#         self.cumulative_frequencies[sorted_symbols[0]] = 0
#         for i in range(1, len(sorted_symbols)):
#             self.cumulative_frequencies[sorted_symbols[i]] = self.cumulative_frequencies[sorted_symbols[i-1]] + self.frequencies[sorted_symbols[i-1]]

#     # def encode(self):
#     #     low = 0
#     #     range_size = 1
#     #     encoded = []
#     #     for symbol in self.message:
#     #         range_size = range_size * self.total_count // self.frequencies[symbol]
#     #         low = low + (range_size * self.cumulative_frequencies[symbol - 1] // self.total_count)
#     #         while True:
#     #             if low // 256 > 0:
#     #                 encoded.append(low // 256)
#     #                 low = low % 256
#     #             else:
#     #                 break
#     #     encoded.append(low)
#     #     return bytes(encoded)

#     def encode(self):
#         low = 0
#         range_size = 1
#         encoded = []
#         sorted_symbols = sorted(self.frequencies.keys())
#         for symbol in self.message:
#             symbol_index = sorted_symbols.index(symbol)
#             range_size = range_size * self.total_count // self.frequencies[symbol]
#             low = low + (range_size * self.cumulative_frequencies[sorted_symbols[symbol_index - 1]] // self.total_count) if symbol_index > 0 else low
#             while True:
#                 if low // 256 > 0:
#                     encoded.append(low // 256)
#                     low = low % 256
#                 else:
#                     break
#         encoded.append(low)
#         return encoded







# csv_path = Path('ANS-tables.csv')


# with open(csv_path, mode="w") as file:

#     file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, ANS_output_csv, runlength_huffman_encoded, ANS_kolmogorov,  ANS_shannon\n")

#     for string_length in range(10, 100):
#         test_str:str = get_random_string(length=8)
#         #     #string_length : str = len(test_str)
#         test_string_kolmogorov: int = kolmogorov(test_str)
#         test_string_shannon: float = shannon(test_str)
#             # ANS_output: list = ANSEncoder(test_str)
#             # ANS_encoded : list = ANS_output.encode()
#         encoder = ANSEncoder(test_str)
#         encoded = encoder.encode()

#         print(encoded)
#         # break

#         runlength_output_csv: str = ""

#         for tuple_items in runlength_output:
#             for tuple_item in tuple_items:
#                 runlength_output_csv += str(tuple_item) + ""
#             runlength_output_csv += ""

#         runlength_huffman_encoded : str = huffman(str(runlength_output_csv))[0]
#         runlength_kolmogorov: int = kolmogorov(runlength_huffman_encoded)
#         runlength_shannon: float = shannon(runlength_huffman_encoded)

#         csv_template : str = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {runlength_output_csv}, {runlength_huffman_encoded}, {runlength_kolmogorov}, { runlength_shannon}\n"

#         print(f"Progress: {string_length} / 100")
#         file.write(csv_template)


#!/usr/bin/env python

from pathlib import Path
from utilities import get_random_string
import sys

sys.path.append("metrics")
sys.path.append("encodings")

from kolmogorov import estimate_kolmogorov_complexity as kolmogorov
from shannon import shannon_entropy as shannon

# Add the import statement for ANSEncoder class
from ANS3 import ANSEncoder

csv_path = Path('ANS-tablesLettersNumbers100.csv')

with open(csv_path, mode="w") as file:
    file.write("string_length, test_str, test_string_kolmogorov, test_string_shannon, ANS_encoded, ANS_kolmogorov, ANS_shannon\n")

    for string_length in range(10, 100):
        test_str = get_random_string(length=string_length)
        test_string_kolmogorov = kolmogorov(test_str)
        test_string_shannon = shannon(test_str)

        # Create an instance of ANSEncoder and encode the test string
        encoder = ANSEncoder(test_str)
        encoded = encoder.encode()

        # Convert the encoded byte array to a string representation
        #ANS_output_csv = ' '.join(map(str, encoded))

        ANS_output_csv = ""

        for tuple_item in encoded:
            ANS_output_csv += str(tuple_item) + " "

        # Calculate the Kolmogorov complexity and Shannon entropy for the ANS encoded message
        ANS_kolmogorov = kolmogorov(ANS_output_csv)
        ANS_shannon = shannon(ANS_output_csv)

        csv_template = f"{string_length}, {test_str}, {test_string_kolmogorov}, {test_string_shannon}, {ANS_kolmogorov}, {ANS_shannon}\n"

        print(f"Progress: {string_length} / 100")
        file.write(csv_template)

