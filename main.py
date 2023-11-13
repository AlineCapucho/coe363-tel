from huffman import huffman_compressor, huffman_decompressor
from text_helpers import get_txt_size

books = [
  {
    'name': 'Dracula',
    'original': './raw-data/dracula.txt',
    'compressed':'./results/dracula-compressed.txt',
    'decompressed': './results/dracula-decompressed.txt',
  },
  {
    'name': 'Le Comte de Monte Cristo',
    'original': './raw-data/le-comte-de-monte-cristo.txt',
    'compressed':'./results/le-comte-de-monte-cristo-compressed.txt',
    'decompressed': './results/le-comte-de-monte-cristo-decompressed.txt',
  },
  {
    'name': 'Dom Casmurro',
    'original': './raw-data/dom-casmurro.txt',
    'compressed': './results/dom-casmurro-compressed.txt',
    'decompressed': './results/dom-casmurro-decompressed.txt',
  },
  {
    'name': 'La Divina Commedia',
    'original': './raw-data/la-divina-commedia.txt',
    'compressed': './results/la-divina-commedia-compressed.txt',
    'decompressed': './results/la-divina-commedia-decompressed.txt',
  },
  {
    'name': '入れかわった男',
    'original': './raw-data/入れかわった男.txt',
    'compressed': './results/入れかわった男-compressed.txt',
    'decompressed': './results/入れかわった男-decompressed.txt',
  },
  {
    'name': 'schumann',
    'original': './raw-data/schumann.txt',
    'compressed': './results/schumann-compressed.txt',
    'decompressed': './results/schumann-decompressed.txt',
  }
]

for book in books:
  huffman_compressor(book['original'], book['compressed'])
  huffman_decompressor(book['original'], book['compressed'], book['decompressed'])

  print(f"\n{book['name']}")
  print('ORIGINAL - sizeof', get_txt_size(book['original']))
  print('COMPRESSED - sizeof', get_txt_size(book['compressed']))
  print('DECOMPRESSED - sizeof', get_txt_size(book['decompressed']))
