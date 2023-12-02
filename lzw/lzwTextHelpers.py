import struct

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        return file.read()

def write_compressed_file(compressed_data, filename):
    with open(filename, 'wb') as file:
        file.write(struct.pack('I' * len(compressed_data), *compressed_data))

def read_compressed_file(filename):
    with open(filename, 'rb') as file:
        # to do: Corrigir este unpack pra ler certinho, consultar prevs.dat do backtest?
        compressed_data = struct.unpack('I' * (len(file.read()) // 2), file.read())
    return compressed_data

def write_decompressed_file(decompressed_data, filename):
    with open(filename, 'w') as file:
        file.write(decompressed_data)