# userinput.py
# Bhavyai Gupta
#
# Class to facilitate the user input for the program "encryption.py",
# and perform checks on the validity of the user input

import re
import colors


class UserInput:
    """
    Class to facilitate the user input and perform validity checks

    Methods:
        check_cipher(self, cipher): Function to check the validity of the parameter - 26 characters long consisting of lower alphanumeric only
        get_choice(self):           Function to get user input to choose to encrypt or decrypt the text
        get_text(self, choice):     Function to receive user input to get the text to be encrypted or decrypted, and process the text for further operations
        get_cipher(self):           Function to receive user input to get the cipher for encryption or decryption
    """

    def check_cipher(self, cipher):
        """
        Function to check the validity of the parameter - 26 characters long consisting of lower alphanumeric only

            Parameters:
                cipher (str): the cipher whose validity needs to be checked

            Returns:
                (bool):       True if cipher is valid and False if cipher is invalid
        """
        cipher = str(cipher)

        if len(cipher) != 26:
            # checking for length of 26
            return False

        elif not cipher.islower():
            # checking for lowercase
            return False

        elif not cipher.isalnum():
            # checking for something other than alphabets and numbers
            return False

        else:
            return True

    def get_choice(self):
        """
        Function to get user input to choose to encrypt or decrypt the text

            Parameters:
                none

            Returns:
                choice (str): "encrypt" if user decides to encode the text or "decrypt" if user decides to decode the text
        """

        print("[{0}INFO{1}] Enter your choice:".format(
            colors.yellow, colors.reset), end=" ")

        while(True):
            temp_choice = input()

            # make comparisons of string after using casefold()
            if temp_choice.casefold() == "e".casefold() or temp_choice.casefold() == "eNcRyPt".casefold():
                choice = "encrypt"
                break

            elif temp_choice.casefold() == "d".casefold() or temp_choice.casefold() == "DeCrYpT".casefold():
                choice = "decrypt"
                break

            else:
                print("[{0}FAIL{1}] Incorrect choice!\n".format(
                    colors.red, colors.reset))
                print(
                    "[{0}NOTE{1}] You must enter either encrypt/e or decrypt/d\n".format(colors.cyan, colors.reset))
                print("[{0}INFO{1}] Please enter your choice again:".format(
                    colors.yellow, colors.reset), end=" ")
                continue

        return choice

    def get_text(self, choice):
        """
        Function to receive user input to get the text to be encrypted or decrypted, and process the text for further operations

            Parameters:
                choice (str):       the choice user has made - either encrypt or decrypt

            Returns:
                cleaned_text (str): the text by removing non-alphanumeric characters and converting it into lowercase in case of encryption
        """

        print("[{0}INFO{1}] Enter the text below that you want to {2}:\n".format(
            colors.yellow, colors.reset, choice))

        text = input()
        cleaned_text = ""

        # for encoding, keep only alphabets and remove everything else. Then convert to lowercase
        if choice == "encrypt":
            # compile the regular expression to use only alphabetic characters
            regex = re.compile('[a-zA-Z]+')
            # regex.findAll() will return a list of all individual characters. join() them into a string, and then convert to lowercase
            cleaned_text = cleaned_text.join(regex.findall(text)).lower()

        # for decoding, string should not be touched
        else:
            cleaned_text = text

        return cleaned_text

    def get_cipher(self):
        """
        Function to receive user input to get the cipher for encryption or decryption

            Parameters:
                none

            Returns:
                cipher (str): the cipher entered by the user, after validity checks
        """

        print("\n[{0}INFO{1}] Requesting cipher to proceed\n".format(
            colors.yellow, colors.reset))

        while(True):
            try:
                print("[{0}NOTE{1}] Please note that the cipher must be 26 characters long, containing only lowercase alphabets and/or digits only\n".format(colors.cyan, colors.reset))

                print("[{0}INFO{1}] Enter the cipher now: ".format(
                    colors.yellow, colors.reset), end="")
                cipher = input()

                # check the validity of cipher or raise ValueError
                if(self.check_cipher(cipher)):
                    break

                else:
                    raise ValueError("[{0}FAIL{1}] Invalid cipher".format(
                        colors.red, colors.reset))

            except ValueError as err:
                print(err)
                print("[{0}INFO{1}] Requesting cipher again to proceed\n".format(
                    colors.yellow, colors.reset))

        return cipher
