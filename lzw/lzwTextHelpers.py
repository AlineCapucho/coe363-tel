import struct

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        return file.read()

def write_compressed_file(compressed_data, filename):
    packed_data = struct.pack('I' * len(compressed_data), *compressed_data)
    with open(filename, 'wb') as file:
        file.write(packed_data)

def read_compressed_file(filename):
    with open(filename, 'rb') as file:
        read_data = file.read()
    compressed_data = struct.unpack('I' * (len(read_data) // 4), read_data)
    return list(compressed_data)

def write_decompressed_file(decompressed_data, filename):
    with open(filename, 'w') as file:
        file.write(decompressed_data)