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

def __encoder(original_string):
  """Given a string, return a binary encoded version of it using the Huffman algorithm."""
  
  freq_dict = __get_frequency(original_string)
  root = __make_tree(freq_dict)

  code_dict = {}
  __make_code(root, "", code_dict)
  
  encoded = ""
  for symbol in original_string:
    encoded = encoded + str(code_dict[symbol])

  return encoded

def __compressor(encoded_string):
  """Given an encoded binary string, breaks it into segments of 8 bits each and converts these segments to bytes. Return the string in bytes"""
  
  compressed_bits = [encoded_string[i:i+8] for i in range(0, len(encoded_string), 8)]
  compressed_bytes = bytes([int(b, 2) for b in compressed_bits])

  return compressed_bytes

def __decompressor(compressed_bytes):
  """Given a bytes value representing a binary string, return the original binary string"""
  
  binary_str = ''.join(format(byte, '08b') for byte in compressed_bytes)
  
  return binary_str

def __decoder(compressed_bytes):
  """"""
  binary_str = __decompressor(compressed_bytes)

# given the encoded result and the root
# transverse the tree and decode it
# return the original text
def __tree_decoder(binary_str, root):
  """"""
  decoded_str = ""

  current_node = root
  for bit in binary_str:
      if bit == '0':
          current_node = current_node.left
      else:
          current_node = current_node.right

      if current_node.left is None and current_node.right is None:
          decoded_str += current_node.data
          current_node = root

  return decoded_str
