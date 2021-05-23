# encryption.py
# Bhavyai Gupta
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc.
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

from encode import Encode
import re


def main():
    print("Welcome to Encryption Program")

    print("What do you want to try today: Encryption or Decryption?")
    print()
    print("Enter e or encode or encryption for Encryption")
    print("Enter d or decode or decryption for Decryption")

    print("Enter your choice:", end=" ")

    while(True):
        try:
            choice = input()

            if choice.casefold() == "e".casefold() or choice.casefold() == "encrypt".casefold() or choice.casefold() == "ENCRYPTION".casefold():
                pass
                break

            elif choice.casefold() == "d".casefold() or choice.casefold() == "decrypt".casefold() or choice.casefold() == "DECRYPTION".casefold():
                pass
                break

            else:
                raise ValueError

        except ValueError:
            print("Incorrect choice! Please enter your choice again:", end=" ")
            continue




# if __name__ == '__main__':
#     main()



def test():
    # user inputs
    text = "Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin"
    cipher = "bcdefghijklmnopqrstuvwxyza"


    # user inputs for decode
    text = "uifcftuboenptucfbvujgvmuijohtjouifxpsmedboopucftffopsfwfoupvdifeuifznvtucfgfmuxjuiuififbsuifmfolfmmfs"
    cipher = "bcdefghijklmnopqrstuvwxyza"


    regex = re.compile('\w')
    cleaned_text = ""
    cleaned_text = cleaned_text.join(regex.findall(text.lower()))

    # alternate way of cleaning the input text
    # cleaned_text = "".join(re.findall("[a-zA-Z0-9]+", text))
    # cleaned_text = regex.findall(text)

    encode = Encode(cipher, cleaned_text)
    # print(encode.encrypt())
    print(encode.decrypt())


test()

