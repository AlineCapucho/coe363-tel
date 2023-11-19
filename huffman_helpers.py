import json

class huffman_node:
  """Represents a node in a Huffman tree. Data -> symbol. Freq -> Frequency of data"""
  def __init__(self, data, freq):
    self.data = data
    self.freq = freq
    self.left = None
    self.right = None

def __get_frequency(string):
  """Given a string, returns a dictionary with the frequency of its characters"""
  
  freq_dict = {}
  
  for symbol in (string):
    if symbol in freq_dict.keys():
      freq_dict[symbol] += 1
    else:
      freq_dict[symbol] = 1

  return freq_dict

def __make_tree(freq_dict):
  """Given a character frequency dictionary, make a huffman tree and return its root"""
  
  nodes = []

  for item in freq_dict.items():
    node = huffman_node(item[0], item[1])
    nodes.append(node)

  if len(nodes) > 1:
    while len(nodes) > 1:
      sorted_nodes = sorted(nodes, key = lambda node: node.freq)
      node1, node2 = sorted_nodes[0], sorted_nodes[1]
      parent = huffman_node('-', node1.freq + node2.freq)
      parent.left = node1            
      parent.right = node2
      root = parent
      nodes.remove(node1)
      nodes.remove(node2)
      
      nodes.append(parent)
  else:
    root = nodes[0]
  
  return root

def __make_code(node, code, encoded_dict):
  """Given a character frequency dict and the root of a huffman tree, return a dictionary of the huffman codification for the characters"""
  
  if node.left == None and node.right == None:
    encoded_dict[node.data] = code
    return encoded_dict

  __make_code(node.right, code+"1",encoded_dict)
  __make_code(node.left, code+"0",encoded_dict)

def __dict_compressor(encoded_dict):
  dict_to_str = ''.join(format(ord(char), '8b') for char in json.dumps(encoded_dict))
  compressed_bits = [dict_to_str[i:i+8] for i in range(0, len(dict_to_str), 8)]
  compressed_bytes = bytes([int(b, 2) for b in compressed_bits])

  return compressed_bytes

def __encoder(original_string):
  """Given a string, return a binary encoded version of it using the Huffman algorithm."""
  
  freq_dict = __get_frequency(original_string)
  root = __make_tree(freq_dict)

  code_dict = {}
  code_dict['code_dict'] = 'true'
  __make_code(root, "", code_dict)
  
  encoded = ""
  for symbol in original_string:
    encoded = encoded + str(code_dict[symbol])

  return [encoded, code_dict]

def __compressor(encoded_string):
  """Given an encoded binary string, breaks it into segments of 8 bits each and converts these segments to bytes. Return the string in bytes"""
  
  compressed_bits = [encoded_string[i:i+8] for i in range(0, len(encoded_string), 8)]
  
  for i in range(len(compressed_bits)):
    length = len(compressed_bits[i])
    if (length != 8):
      compressed_bits[i] += '0'*(8 - length)

  compressed_bytes = bytes([int(b, 2) for b in compressed_bits])
  
  return compressed_bytes

def __decompressor(compressed_bytes):
  """Given a bytes value representing a binary string, return the original binary string"""
  code_dict_index = compressed_bytes.rindex(b'code_dict') - 2
  code_dict_compressed = compressed_bytes[slice(code_dict_index, len(compressed_bytes))]
  code_dict_encoded = ''.join(format(byte, '08b') for byte in code_dict_compressed)

  compressed_str = compressed_bytes[slice(0, code_dict_index)]
  encoded_str = ''.join(format(byte, '08b') for byte in compressed_str)

  return [encoded_str, code_dict_encoded]

def __decoder(binary_str, code_dict):
  """Given a binary string and the encoding dictionary, return the original string"""
  inverted_code_dict = {value: key for key, value in code_dict.items()}
  
  current_character = ""
  decoded_str = ""

  for bit in binary_str:
    current_character += bit
    if current_character in inverted_code_dict:
      decoded_str += inverted_code_dict[current_character]
      current_character = ""

  return decoded_str.strip()
