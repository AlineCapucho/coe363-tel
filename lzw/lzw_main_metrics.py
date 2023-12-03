from lzw import LZWCompression
from lzwTextHelpers import read_compressed_file, read_file, write_compressed_file, write_decompressed_file
from text_helpers import get_txt_size
import time
from matplotlib import pyplot as plt
import numpy as np  

books = [
  {
    'name': 'Dracula',
    'original': './raw-data/dracula.txt',
    'compressed':'./lzw_results/dracula-compressed.txt',
    'decompressed': './lzw_results/dracula-decompressed.txt',
  },
  {
    'name': 'Le Comte de Monte Cristo',
    'original': './raw-data/le-comte-de-monte-cristo.txt',
    'compressed':'./lzw_results/le-comte-de-monte-cristo-compressed.txt',
    'decompressed': './lzw_results/le-comte-de-monte-cristo-decompressed.txt',
  },
  {
    'name': 'Dom Casmurro',
    'original': './raw-data/dom-casmurro.txt',
    'compressed': './lzw_results/dom-casmurro-compressed.txt',
    'decompressed': './lzw_results/dom-casmurro-decompressed.txt',
  },
  {
    'name': 'La Divina Commedia',
    'original': './raw-data/la-divina-commedia.txt',
    'compressed': './lzw_results/la-divina-commedia-compressed.txt',
    'decompressed': './lzw_results/la-divina-commedia-decompressed.txt',
  },
  {
    'name': 'schumann',
    'original': './raw-data/schumann.txt',
    'compressed': './lzw_results/schumann-compressed.txt',
    'decompressed': './lzw_results/schumann-decompressed.txt',
  }
]

original_sizes, compressed_sizes, decompressed_sizes = [], [], []
compression_rates, decompression_rates = [], []
compression_times, decompression_times = [], []

for book in books:
  compressor = LZWCompression()
  start_time = time.time()
  input_text = read_file(book["original"])
  compressed_data = compressor.compress(input_text)
  write_compressed_file(compressed_data, book['compressed'])
  execution_time = time.time() - start_time

  compression_times.append(execution_time)

  start_time = time.time()
  compressed_file = read_compressed_file(book['compressed'])
  decompressed_data = compressor.decompress(compressed_file)
  write_decompressed_file(decompressed_data, book['decompressed'])
  execution_time = time.time() - start_time

  decompression_times.append(execution_time)

  original_size = get_txt_size(book['original'])
  compressed_size = get_txt_size(book['compressed'])
  decompressed_size = get_txt_size(book['decompressed'])

  original_sizes.append(original_size) 
  compressed_sizes.append(compressed_size) 
  decompressed_sizes.append(decompressed_size)

  compression_rates.append((compressed_size/original_size)*100)
  decompression_rates.append((decompressed_size/original_size)*100)
  
book_names = [book['name'] for book in books]

# Compression Time Plot
print(f'Taxa de compressão média: {np.mean(compression_rates): .2f}%')
print(f'Taxa de descompressão média: {np.mean(decompression_rates): .2f}%')
print(f'Tempo médio de compressão: {np.mean(compression_times): .2f} segundos')
print(f'Tempo médio de descompressão: {np.mean(decompression_times): .2f} segundos')
print(f'Kbs comprimidos por segundo: {np.sum(original_sizes)/np.sum(compression_times): .2f} kbs/s')

# plt.style.use('seaborn-v0_8-pastel')

X_axis = np.arange(len(book_names)) 

# Compression & Decompression Rates Plot
plt.bar(X_axis - 0.2, compression_rates, 0.4, label = 'Taxa de compressão (%)')
plt.bar(X_axis + 0.2, decompression_rates, 0.4, label = 'Taxa de descompressão (%)')
plt.xticks(X_axis, book_names)
plt.legend()
plt.xlabel('Arquivos')
plt.title('Taxas de compressão e descompressão')
plt.show()

# Original Size vs Compressed Size vs Decompressed Size Plot
plt.bar(X_axis - 0.2, compressed_sizes, 0.2, label = 'Comprimido')
plt.bar(X_axis, decompressed_sizes, 0.2, label = 'Descomprimido')
plt.bar(X_axis + 0.2, original_sizes, 0.2, label = 'Original')
plt.xlabel('Arquivos')
plt.ylabel('Tamanho')
plt.legend()
plt.title('Tamanho dos arquivos - Comprimido x Descomprimido x Original')
plt.show()
True