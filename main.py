from art import logo
from alphabet_list import alphabet

"""
TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. """

def init():
    print(logo)

def caesar(plain_text, shift_amount, caesar_type):
    cipher_text = ""

    if caesar_type == "decode":
        if shift_amount > 26:
            shift_amount = shift_amount % 26
        print(shift_amount)
        shift_amount *= -1
        print(shift_amount)

    elif caesar_type == "encode":
        #This is to adjust if the number is greater than 26 and it will adjust to be within the spectrum of the alphabet list.
        if shift_amount > 26:
            shift_amount = shift_amount % 26
            print(shift_amount)

    for char in plain_text:
        #NOw it will check if the char is in the alphabet list otherwise it will keep as it is and add in the end message.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char

    print(f"The {caesar_type}d text is {cipher_text}")

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

init()
program_on = True

while program_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, caesar_type=direction)

    restart_software = input("Do you want to restart app?:\nType \"Yes\" or \"No\"").lower()

    if restart_software == "no":
        program_on = False
        print('Thanks for Using Caesar Cipher!!!')
    else:
        print(logo)