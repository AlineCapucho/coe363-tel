from huffmanHelpers import getSymbolFreq, createNodes, getTreeRoot, makeCode

# given the original text
# create the symbols dictionary
# use it to create the huffman nodes
# create the huffman tree
# represent each character through a code
# return the encoded text
def encoder(originalString):
  symbolsDict = getSymbolFreq(originalString)
  nodes = createNodes(symbolsDict)
  root = getTreeRoot(nodes)

  codeDict = {}
  makeCode(root, "", codeDict)
  
  encoded = ""
  for symbol in originalString:
    encoded = encoded + str(codeDict[symbol])

  return encoded

# given the encoded result and the root
# transverse the tree and decode it
# return the original text
def decodeFromTree(encodedText, root):
  decoded = ""
  currentNode = root

  for i in range(len(encodedText)):
    if encodedText[i] == '0':
      currentNode = currentNode.left
    else:
      currentNode = currentNode.right

    if currentNode.left == None and currentNode.right == None:
      decoded += currentNode.data
      currentNode = root
  
  return decoded
