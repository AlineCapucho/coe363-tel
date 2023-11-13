from huffman_helpers import __encoder, __compressor, __decompressor, __tree_decoder, __get_frequency, __make_tree
from text_helpers import txt_to_str, byte_to_txt, str_to_txt, txt_to_byte

def huffman_compressor(original_file_name, compressed_file_name):
  """Given a txt file, compress it using the Huffman algorithm and write it to a new txt file"""
  
  original_str = txt_to_str(original_file_name)
  encoded_str = __encoder(original_str)
  compressed_str = __compressor(encoded_str)

  byte_to_txt(compressed_str, compressed_file_name)

def huffman_decompressor(original_file_name, compressed_file_name, decompressed_file_name):
  """Given a txt file compressed using the Huffman algorithm, decompress it and write the original to a new txt file"""

  original_str = txt_to_str(original_file_name)

  compressed_str = txt_to_byte(compressed_file_name)
  decompressed_str = __decompressor(compressed_str)

  freq_dict = __get_frequency(original_str)
  root = __make_tree(freq_dict)

  decoded_str = __tree_decoder(decompressed_str, root)

  str_to_txt(decoded_str, decompressed_file_name)