class LZWCompression:
    def __init__(self):
        self.compress_dict_size = 65536 #unicode
        self.decompress_dict_size = 65536 #unicode
        self.compress_dictionary = {chr(i): i for i in range(self.compress_dict_size)}
        self.decompress_dictionary = {i: chr(i) for i in range(self.decompress_dict_size)}
        self.next_code = 65536

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


    def decompress(self, compressed: list[int]):
        from io import StringIO

        result = StringIO()
        w = chr(compressed.pop(0))
        result.write(w)
        for k in compressed:
            if k in self.decompress_dictionary:
                entry = self.decompress_dictionary[k]
            elif k == self.decompress_dict_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compressed k: %s' % k)
            result.write(entry)

            self.decompress_dictionary[self.decompress_dict_size] = w + entry[0]
            self.decompress_dict_size += 1

            w = entry
        return result.getvalue()