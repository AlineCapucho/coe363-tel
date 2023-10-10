from textHelpers import txtToString, stringToTxt
from huffmanHelpers import getSymbolFreq, createNodes, getTreeRoot
from huffman import encoder, decodeFromTree

dracula = './raw-data/dracula.txt'
# monteCristo = './raw-data/le-comte-de-monte-cristo.txt'
# domCasmurro = './raw-data/dom-casmurro.txt'

originalString = txtToString(dracula)

encoded = encoder(originalString)

stringToTxt(encoded, './results/dracula-encoded.txt')

symbolsDict = getSymbolFreq(originalString)
nodes = createNodes(symbolsDict)
root = getTreeRoot(nodes)

decoded = decodeFromTree(encoded, root)

stringToTxt(decoded, './results/dracula-decoded.txt')
