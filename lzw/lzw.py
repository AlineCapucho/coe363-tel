from io import StringIO

class LZWCompression:
    def __init__(self):
        self.compress_dict_size = 65536 # Unicode
        self.decompress_dict_size = 65536 # Unicode
        self.compress_dictionary = {chr(i): i for i in range(self.compress_dict_size)}
        self.decompress_dictionary = {i: chr(i) for i in range(self.decompress_dict_size)}
        self.next_code = 65536

    def compress(self, uncompressed: str):
        current_sequence = ""
        result = []
        for current_char in uncompressed:
            new_sequence = current_sequence + current_char
            if new_sequence in self.compress_dictionary:
                current_sequence = new_sequence
            else:
                result.append(self.compress_dictionary[current_sequence])
                self.compress_dictionary[new_sequence] = self.compress_dict_size
                self.compress_dict_size += 1
                current_sequence = current_char

        if current_sequence:
            result.append(self.compress_dictionary[current_sequence])
        return result

    def decompress(self, data):
        result = StringIO()
        current_code = chr(data.pop(0))
        result.write(current_code)

        for code in data:
            if code in self.decompress_dictionary:
                entry = self.decompress_dictionary[code]
            elif code == self.next_code:
                entry = current_code + current_code[0]
            else:
                raise ValueError(f"Bad compressed code: {code}")

            result.write(entry)
            self.decompress_dictionary[self.next_code] = current_code+ entry[0]
            self.next_code += 1
            current_code = entry

        return result.getvalue()