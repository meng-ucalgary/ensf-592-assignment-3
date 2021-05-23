# crypto.py
# Bhavyai Gupta
#
# Class to provide methods for encryption and decryption for the program "encryption.py"


class Crypto:
    """
    Class to provide methods for encryption and decryption

    Attributes:
        __cipher (str): the cipher to be used for encryption or decryption
        __alphabets (list): a list of individual characters of alphabets
        __encoding_dict (dictionary): dictionary with alphabets as key and corresponding substitution cipher as value
        __decoding_dict (dictionary): dictionary with substitution cipher as key and alphabets as value

    Methods:
        __init__(self, cipher): Constructor to initialize __cipher, create list of alphabets, and dictionaries mapping alphabets and cipher
        encrypt(self, text): Function to encrypt the parameter using the cipher
        decrypt(self, text): Function to decrypt the parameter using the cipher
    """
    __cipher = ""

    def __init__(self, cipher):
        """
        Constructor to initialize __cipher, create list of alphabets, and dictionaries mapping alphabets and cipher

        Parameters:
            cipher (str): the cipher to be used to encode or decode a message

        Returns:
            None
        """
        self.__cipher = cipher

        # a list of individual characters of alphabets
        self.__alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]

        # dictionary with alphabets as key and corresponding substitution cipher as value
        self.__encoding_dict = dict(zip(self.__alphabets, self.__cipher))

        # dictionary with substitution cipher as key and alphabets as value
        self.__decoding_dict = dict(zip(self.__cipher, self.__alphabets))

    def encrypt(self, text):
        """
        Function to encrypt the parameter using the cipher

        Parameters:
            text (str): the string to be encrypted

        Returns:
            encrypted_string (str): the encrypted text
        """

        encrypted_string = ""

        for i in text:
            # get the characters from text, get correspoding cipher, and form an encoded string
            encrypted_string += self.__encoding_dict.get(i)

        return encrypted_string

    def decrypt(self, text):
        """
        Function to decrypt the parameter using the cipher

        Parameters:
            text (str): the string to be decrypted

        Returns:
            decrypted_string (str): the decrypted text
        """
        decrypted_string = ""

        for i in text:
            # get the characters from encoded text, get correspoding decoded character, and form a decoded string
            decrypted_string += self.__decoding_dict.get(i)

        return decrypted_string
