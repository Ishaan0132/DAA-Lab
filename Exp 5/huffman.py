import heapq
from collections import defaultdict

class Node:
    """A node in the Huffman tree."""
    
    def __init__(self, char, freq):
        """Initialize a node with a character and frequency."""
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Less-than comparison for heapq."""
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    """Builds the Huffman tree and returns the root node."""
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]  # The root of the Huffman tree

def generate_codes(node, prefix='', codebook=None):
    """Generates Huffman codes for the characters in the tree."""
    if codebook is None:
        codebook = {}
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(data):
    """Encodes the input string using Huffman coding."""
    if not isinstance(data, str):
        print("Input must be a string.")
        return None, None
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_codes(huffman_tree)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes

def calculate_compression_ratio(original, encoded):
    """Calculates the compression ratio."""
    original_size = len(original) * 8  # Assuming 8 bits per character
    compressed_size = len(encoded)  # Length of the encoded string
    print(original_size, compressed_size)
    if compressed_size == 0:
        print('Input file has no text')
        return None  # Handle division by zero
    return compressed_size / original_size

def save_compressed_data(encoded_data, output_file):
    """Saves the encoded data to a file, packing the bits into bytes."""
    # Convert the string of bits into actual bytes
    byte_data = bytearray()
    for i in range(0, len(encoded_data), 8):
        byte = encoded_data[i:i+8]
        byte_data.append(int(byte, 2))  # Convert each 8 bits to a byte
    
    # Save the byte data to the file
    with open(output_file, 'wb') as file:
        file.write(byte_data)
    print(f"Compressed data saved to {output_file}")


def run_huffman_test(file_path, output_file):
    """Runs Huffman encoding on the given file, saves the result to a new file, and prints results."""
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if len(data) == 0:
                print("File is empty")
                return
            encoded_data, huffman_codes = huffman_encoding(data)
            compression_ratio = calculate_compression_ratio(data, encoded_data)
            print(f"Test for file: {file_path}")
            # print("Encoded Data:", encoded_data)
            print("Huffman Codes:", huffman_codes)
            print("Compression Ratio:", compression_ratio)
            print("-" * 40)
            
            # Save the compressed data to the output file
            save_compressed_data(encoded_data, output_file)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run tests on specified files and save the compressed output
if __name__ == "__main__":
    run_huffman_test('large_input.txt', 'output_compressed_large.bin')
    run_huffman_test('test1.txt', 'output_compressed_1.txt')
    run_huffman_test('test2.txt', 'output_compressed_2.txt')
    run_huffman_test('test3.txt', 'output_compressed_3.txt')
    run_huffman_test('test4.txt', 'output_compressed_4.txt')
    run_huffman_test('test5.txt', 'output_compressed_5.txt')
    run_huffman_test('test6.txt', 'output_compressed_6.txt')
