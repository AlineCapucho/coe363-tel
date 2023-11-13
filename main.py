from textHelpers import txtToString, byteStringToTxt, stringToTxt, txtFileSize
from huffmanHelpers import getSymbolFreq, createNodes, getTreeRoot
from huffman import encoder, decodeFromTree

dracula = './raw-data/dracula.txt'
# monteCristo = './raw-data/le-comte-de-monte-cristo.txt'
# domCasmurro = './raw-data/dom-casmurro.txt'

originalString = txtToString(dracula)
compressed = encoder(originalString)

byteStringToTxt(compressed, './results/dracula-compressed.txt')

symbolsDict = getSymbolFreq(originalString)
nodes = createNodes(symbolsDict)
root = getTreeRoot(nodes)
decoded = decodeFromTree(compressed, root)

stringToTxt(decoded, './results/dracula-decompressed.txt')

print('ORIGINAL - sizeof', txtFileSize('./raw-data/dracula.txt'))
print('COMPRESSED - sizeof', txtFileSize('./results/dracula-compressed.txt'))
print('DECOMPRESSED - sizeof', txtFileSize('./results/dracula-decompressed.txt'))