# represents a node in the huffman tree
# data is the symbol represented by the node
# freq is the frequency of the data
# left and right are the children of that node
class huffmanNode:
  def __init__(self, data, freq):
    self.data = data
    self.freq = freq
    self.left = None
    self.right = None

# given a string, return a dictionary
# with the frequency of all characters/symbols
# present in the string
def getSymbolFreq(originalString):
  dict = {}
  for symbol in (originalString):
    if symbol in dict.keys():
      dict[symbol] += 1
    else:
      dict[symbol] = 1

  return dict

# given a dict of symbol frequencies
# create a huffmanNode out of every dict entry
def createNodes(dict):
  nodes = []

  for item in dict.items():
    node = huffmanNode(item[0], item[1])
    nodes.append(node)

  return nodes

# given a list of nodes
# mount the huffman tree
# and return the root of the tree
def getTreeRoot(nodes):
  if len(nodes) > 1:
    while len(nodes) > 1:
      sortedNodes = sorted(nodes, key = lambda node: node.freq)
      node1, node2 = sortedNodes[0], sortedNodes[1]
      parent = huffmanNode('-', node1.freq + node2.freq)
      parent.left = node1            
      parent.right = node2
      root = parent
      nodes.remove(node1)
      nodes.remove(node2)
      
      nodes.append(parent)
  else:
    root = nodes[0]
  
  return root

# codify every huffman tree node starting from the root(recursive)
# for every right transversal, add "1" to the code
# for every left transversal, add "0" to the code
# if the node has no right and no left children
# then it's a leaf node (symbol)
def makeCode(node, code, dict):
  if node.left == None and node.right == None:
    dict[node.data] = code
    return dict

  makeCode(node.right, code+"1",dict)
  makeCode(node.left, code+"0",dict)