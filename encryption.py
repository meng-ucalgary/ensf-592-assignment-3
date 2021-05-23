# encryption.py
# Bhavyai Gupta
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc.
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

from crypto import Crypto
from userinput import UserInput
import colors


def main():
    """
    Function to serve as a TUI front-end of the encryption program
    """
    print("\n\nWelcome to Encryption Program")
    print("-----------------------------\n")

    user_input = UserInput()

    print("\n[{0}INFO{1}] What do you want to try today: Encryption or Decryption?\n".format(
        colors.yellow, colors.reset))
    print("[{0}NOTE{1}] For Encryption : enter either e or encrypt".format(
        colors.cyan, colors.reset))
    print("[{0}NOTE{1}] For Decryption : enter either d or decrypt\n".format(
        colors.cyan, colors.reset))

    # get the choice from the user for encryption or decryption
    choice = user_input.get_choice()

    # if: user chooses encryption, else: user chooses decryption
    if choice == "encrypt":
        # get the text to be encoded
        text = user_input.get_text(choice)

        # get the cipher to use for encoding
        cipher = user_input.get_cipher()

        # create an object of class Crypto to use its function encrypt()
        code = Crypto(cipher)
        print("\n[{0}DONE{1}] Encoded text is\n\n{2}".format(
            colors.green, colors.reset, code.encrypt(text)))

    else:
        # get the text to be decoded
        text = user_input.get_text(choice)

        # # get the cipher to use for decoding
        cipher = user_input.get_cipher()

        # create an object of class Crypto to use its function decrypt()
        code = Crypto(cipher)
        print("\n[{0}DONE{1}] Decoded text is\n\n{2}".format(
            colors.green, colors.reset, code.decrypt(text)))

    # print see-off message to let user know program has terminated
    print("\n\n{0}Bye!{1}".format(colors.green, colors.reset))


if __name__ == '__main__':
    main()
