class Encode:
    def __init__(self, cipher, text):
        self.cipher = cipher
        self.cipher_list = [i for i in cipher]
        self.text = text
        self.alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
        self.encoding_dict = dict(zip(self.alphabets, self.cipher_list))
        self.decoding_dict = dict(zip(self.cipher_list, self.alphabets))


    def encrypt(self):
        encrypted_string = ""

        for i in self.text:
            encrypted_string += self.encoding_dict.get(i)

        return encrypted_string


    def decrypt(self):
        decrypted_string = ""

        for i in self.text:
            decrypted_string += self.decoding_dict.get(i)

        return decrypted_string

