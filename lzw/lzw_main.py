from lzwTextHelpers import read_compressed_file, read_file, write_compressed_file, write_decompressed_file
from lzw import LZWCompression

input_filename = "raw-data/le-comte-de-monte-cristo.txt"
compressed_filename = "lzw_results/le-comte-de-monte-cristo_lzw_encoded.txt"
decompressed_filename = "lzw_results/le-comte-de-monte-cristo_lzw_decoded.txt"
compressor = LZWCompression()

input_text = read_file(input_filename)

compressed_data = compressor.compress(input_text)
write_compressed_file(compressed_data, compressed_filename)

compressed_file = read_compressed_file(compressed_filename)
decompressed_data = compressor.decompress(compressed_file)
write_decompressed_file(decompressed_data, decompressed_filename)

True