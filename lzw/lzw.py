import struct

class LZWCompression:
    def __init__(self):
        self.compress_dict_size = 65536 # Unicode
        self.decompress_dict_size = 65536 # Unicode
        self.compress_dictionary = {chr(i): i for i in range(self.compress_dict_size)}
        self.decompress_dictionary = {i: chr(i) for i in range(self.decompress_dict_size)}
        self.next_code = 256

    def compress(self, uncompressed: str):
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in self.compress_dictionary:
                w = wc
            else:
                result.append(self.compress_dictionary[w])
                self.compress_dictionary[wc] = self.compress_dict_size
                self.compress_dict_size += 1
                w = c

        if w:
            result.append(self.compress_dictionary[w])
        return result

    def decompress(self, compressed: bytes):
        from io import BytesIO

        compressed_data = struct.unpack('I' * (len(compressed) // 4), compressed)

        result = BytesIO()
        w = struct.pack('I', compressed_data.pop(0))
        result.write(w)
        for k in compressed_data:
            if k in self.decompress_dictionary:
                entry = self.decompress_dictionary[k]
            elif k == self.decompress_dict_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)

            entry_bytes = entry.encode('utf-16-le')
            result.write(entry_bytes)

            self.decompress_dictionary[self.decompress_dict_size] = w + entry[0].encode('utf-16-le')
            self.decompress_dict_size += 1

            w = entry_bytes

        return result.getvalue().decode('utf-16-le')