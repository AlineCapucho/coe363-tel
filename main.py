from huffman import huffman_compressor, huffman_decompressor
from text_helpers import get_txt_size

dracula = './raw-data/dracula.txt'
dracula_compressed = './results/dracula-compressed.txt'
dracula_decompressed = './results/dracula-decompressed.txt'

monteCristo = './raw-data/le-comte-de-monte-cristo.txt'
monteCristo_compressed = './results/le-comte-de-monte-cristo-compressed.txt'
monteCristo_decompressed = './results/le-comte-de-monte-cristo-decompressed.txt'

domCasmurro = './raw-data/dom-casmurro.txt'
domCasmurro_compressed = './results/dom-casmurro-compressed.txt'
domCasmurro_decompressed = './results/dom-casmurro-decompressed.txt'

huffman_compressor(dracula, dracula_compressed)
huffman_decompressor(dracula, dracula_compressed, dracula_decompressed)

huffman_compressor(monteCristo, monteCristo_compressed)
huffman_decompressor(monteCristo, monteCristo_compressed, monteCristo_decompressed)

huffman_compressor(domCasmurro, domCasmurro_compressed)
huffman_decompressor(domCasmurro, domCasmurro_compressed, domCasmurro_decompressed)

print('\nDRACULA')
print('ORIGINAL - sizeof', get_txt_size(dracula))
print('COMPRESSED - sizeof', get_txt_size(dracula_compressed))
print('DECOMPRESSED - sizeof', get_txt_size(dracula_decompressed))

print('\nMONTE CRISTO')
print('ORIGINAL - sizeof', get_txt_size(monteCristo))
print('COMPRESSED - sizeof', get_txt_size(monteCristo_compressed))
print('DECOMPRESSED - sizeof', get_txt_size(monteCristo_decompressed))

print('\nDOM CASMURRO')
print('ORIGINAL - sizeof', get_txt_size(domCasmurro))
print('COMPRESSED - sizeof', get_txt_size(domCasmurro_compressed))
print('DECOMPRESSED - sizeof', get_txt_size(domCasmurro_decompressed))