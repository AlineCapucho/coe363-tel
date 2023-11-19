from huffman_helpers import __encoder, __compressor, __decompressor, __decoder, __dict_compressor
from text_helpers import txt_to_str, byte_to_txt, str_to_txt, txt_to_byte
import json

def huffman_compressor(original_file_name, compressed_file_name):
  """Given a txt file, compress it using the Huffman algorithm and write it to a new txt file"""
  
  original_str = txt_to_str(original_file_name)
  encoded_result = __encoder(original_str)

  encoded_str = encoded_result[0]
  code_dict = encoded_result[1]

  compressed_str = __compressor(encoded_str)
  compressed_str += __dict_compressor(code_dict)

  byte_to_txt(compressed_str, compressed_file_name)

def huffman_decompressor(compressed_file_name, decompressed_file_name):
  """Given a txt file compressed using the Huffman algorithm, decompress it and write the original to a new txt file"""
  
  compressed_result = txt_to_byte(compressed_file_name)
  decompressed_result = __decompressor(compressed_result)

  encoded_str = decompressed_result[0]
  code_dict_encoded = decompressed_result[1]

  code_dict_chunks = [code_dict_encoded[i:i+8] for i in range(0, len(code_dict_encoded), 8)]

  code_dict_str = ''.join([chr(int(chunk, 2)) for chunk in code_dict_chunks])

  code_dict = json.loads(code_dict_str)

  decoded_result = __decoder(encoded_str, code_dict)

  str_to_txt(decoded_result, decompressed_file_name)
