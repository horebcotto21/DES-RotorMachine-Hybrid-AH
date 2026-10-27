import string
from collections import namedtuple
from logging import exception
from random import randint

alpha_to_value = {char: i for i, char in enumerate(string.ascii_uppercase)}
value_to_alpha = {i: char for i, char in enumerate(string.ascii_uppercase)}

# mapping between alphabet and first cylinder and between the other cylinders

""" 
If RotorMachine is going to be used from another file (to use the two encryption algorithms consecutively) 
a class for the rotor machine may be needed
"""

# Real cylinders: 26 numbers each (0-25)
rotor_1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor_2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor_3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

list_of_rotors= [rotor_1,rotor_2,rotor_3]

"""
rotors have lists of numbers
I don't need the relationship list, they relate directly by position/index

to look for index inside rotors, the current rotors offset needs to be stored 
and used in calculation. (index - rotor_offset)mod 26.

Before starting encryption, or decryption each rotor needs to be configured
the top of each list can be used as a key.

keys are three letters
each rotor needs to be rotated until the top values of each rotor
correspond to the letters from the key since a dictionary stores this
the lookup is O(1) only loop

since index is used to look for value in next rotor, lookup is O(1)
The main loop is O(n) where n is length of plaintext

Rotors need to be consistent throughout runs, the original order/ without offset 
should not change between runs. So they should not be created randomly
each run.
steps:
letter from plaintext is read
look for value of letter from plaintext
use value of letter as index in list of first rotor
use value from that index in list of first rotor as index for second rotor
use value from that index in list of second rotor as index for third rotor
use value from third rotor and look for what letter it belongs to
"""

class RotorMachine:
    # still needs to take plaintext as input
    def __init__(self, rotors: list, key: str, ):
        self.rotors = rotors
        # check key length, case
        if len(key) != 3:
            raise "input key is not correct length"
        else:
            self.key = key
            #configure rotors
            # print("C =",alpha_to_value.get("C"))
            rr_1,offset_r1 = self.configure_rotor(rotors[0], key[0])
            # print("\n")
            # print("A =",alpha_to_value.get("A"))
            r_2,offset_r2 = self.configure_rotor(rotors[1], key[1])
            # print("\n")
            # print("B =",alpha_to_value.get("B"))
            r_3,offset_r3 = self.configure_rotor(rotors[2], key[2])

    # @Horeb
    def configure_rotor(self, rotor: list,key: str):
        offset = 0
        if len(key) > 1:
            return "incorrect length, input key should be character only for this rotor"

        for item in rotor:
            # print(rotor)
            if value_to_alpha.get(item) == key:
                break
            else:
                rotor = self.rotate_forward(rotor)
                offset += 1

        return rotor, offset

    # @Horeb
    #example of rotation operation, not correct direction for forward
    def rotate_forward(self, rotor : list) -> list:
        last = len(rotor) - 1
        rotor = rotor[-last:] + rotor[:-last]
        return rotor

    # @Andrea
    def encrypt(self, plaintext: str, key : str):
        ciphertext = ""

        # Set each rotor to its starting position using one letter of the key
        cylinder1, offset1 = self.configure_rotor(self.rotors[0], key[0])
        cylinder2, offset2 = self.configure_rotor(self.rotors[1], key[1])
        cylinder3, offset3 = self.configure_rotor(self.rotors[2], key[2])

        # Main loop to iterate through plaintext
        for letter in plaintext:
            # Spaces are kept as-is and don't rotate the rotors
            if letter == " ":
                ciphertext += letter
                continue

            # Pass the letter forward through the rotors:
            # letter -> number -> rotor 1 -> rotor 2 -> rotor 3 -> letter
            valueofLetter = alpha_to_value.get(letter)
            value_c1 = cylinder1[valueofLetter]   # letter's value is the index in rotor 1
            value_c2 = cylinder2[value_c1]        # rotor 1 output is the index in rotor 2
            value_c3 = cylinder3[value_c2]        # rotor 2 output is the index in rotor 3
            cipher_char = value_to_alpha.get(value_c3)  # rotor 3 output becomes the cipher letter
            ciphertext += cipher_char

            # Step all rotors one position so the next letter uses a new substitution
            cylinder1 = self.rotate_forward(cylinder1)
            cylinder2 = self.rotate_forward(cylinder2)
            cylinder3 = self.rotate_forward(cylinder3)

        return ciphertext

    def decrypt(self, ciphertext: str, key: str):
        plaintext = ""

        # Start from the same rotor positions used for encryption (same key)
        cylinder1, offset1 = self.configure_rotor(self.rotors[0], key[0])
        cylinder2, offset2 = self.configure_rotor(self.rotors[1], key[1])
        cylinder3, offset3 = self.configure_rotor(self.rotors[2], key[2])

        for letter in ciphertext:
            # Spaces are kept as-is and don't rotate the rotors
            if letter == " ":
                plaintext += letter
                continue

            # Reverse the path: rotor 3 -> rotor 2 -> rotor 1
            # Search for the value in each rotor; its index is the value from the previous step
            value_c3 = alpha_to_value.get(letter)
            value_c2 = cylinder3.index(value_c3)
            value_c1 = cylinder2.index(value_c2)
            valueofLetter = cylinder1.index(value_c1)        # index in rotor 1 = original letter value
            plaintext += value_to_alpha.get(valueofLetter)

            # Rotate exactly like encryption so positions stay in sync
            cylinder1 = self.rotate_forward(cylinder1)
            cylinder2 = self.rotate_forward(cylinder2)
            cylinder3 = self.rotate_forward(cylinder3)

        return plaintext

if __name__ == "__main__":
    machine = RotorMachine(list_of_rotors, "CAB")
    print("Key: CAB")
    for message in ["HOPE", "HELLO", "NEW YEAR"]:
        encrypted = machine.encrypt(message, "CAB")
        decrypted = machine.decrypt(encrypted, "CAB")
        print(message, "->", encrypted, "->", decrypted)