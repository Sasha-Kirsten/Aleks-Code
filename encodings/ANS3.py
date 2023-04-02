import sys
from collections import defaultdict

class ANSEncoder:
    def __init__(self, message):
        self.message = message
        self.frequencies = defaultdict(int)
        for symbol in message:
            self.frequencies[symbol] += 1
        self.cumulative_frequencies = {}
        self.total_count = sum(self.frequencies.values())
        self.build_cumulative_frequencies()
    
    def build_cumulative_frequencies(self):
        sorted_symbols = sorted(self.frequencies.keys())
        self.cumulative_frequencies[sorted_symbols[0]] = 0
        for i in range(1, len(sorted_symbols)):
            self.cumulative_frequencies[sorted_symbols[i]] = self.cumulative_frequencies[sorted_symbols[i-1]] + self.frequencies[sorted_symbols[i-1]]

    def encode(self):
        low = 0
        range_size = 1
        encoded = []
        sorted_symbols = sorted(self.frequencies.keys())
        for symbol in self.message:
            symbol_index = sorted_symbols.index(symbol)
            range_size = range_size * self.total_count // self.frequencies[symbol]
            low = low + (range_size * self.cumulative_frequencies[sorted_symbols[symbol_index - 1]] // self.total_count) if symbol_index > 0 else low
            while True:
                if low // 256 > 0:
                    encoded.append(low // 256)
                    low = low % 256
                else:
                    break
        encoded.append(low)
        return encoded


if __name__ == '__main__':
    #message = 'baddeedcba'
    message = '$|(4?Cz-)Dd7BN#>GW^i'
    encoder = ANSEncoder(message)
    encoded = encoder.encode()
    print(f"Encoded message: {encoded}")

















