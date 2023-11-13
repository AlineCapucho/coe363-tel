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

  compressedBits = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
  compressedBytes = bytes([int(b, 2) for b in compressedBits])

  return compressedBytes

# given the encoded result and the root
# transverse the tree and decode it
# return the original text
def decodeFromTree(compressedBytes, root):
    binaryString = ''.join(format(byte, '08b') for byte in compressedBytes)
    decodedString = ""

    currentNode = root
    for bit in binaryString:
        if bit == '0':
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

        if currentNode.left is None and currentNode.right is None:
            decodedString += currentNode.data
            currentNode = root

    return decodedString

