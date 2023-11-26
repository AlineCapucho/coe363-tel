def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        return file.read()

def write_compressed_file(compressed_data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, compressed_data)))

def read_compressed_file(filename):
    with open(filename, 'r') as file:
        compressed_data = [int(code) for code in file.read().split() if code.isdigit()]
    return compressed_data

def write_decompressed_file(decompressed_data, filename):
    with open(filename, 'w') as file:
        file.writelines(decompressed_data)