#Python 3.14
# need to create relationship between 3 arrays

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

# Example DO NOT USE
rotor_1 = [2, 3, 4, 1, 0]
rotor_2 = [3,1,2,0,4]
rotor_3 = [4,3,1,2,0]

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

    # TODO parse input/plaintext, remove spaces if any

    # TODO Initial configuration of the 3 rotors numbers from 0-25 each with a unique order




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
    # TODO rotor forward(last element to top) and
    #example of rotation operation, not correct direction for forward
    def rotate_forward(self, rotor : list) -> list:
        last = len(rotor) - 1
        rotor = rotor[-last:] + rotor[:-last]
        return rotor
    # TODO reverse rotate (top element to bottom)


    # @Andrea
    # TODO encrypt function uses loop to iterate through plaintext, and encrypt one letter at a time
    def encrypt(self, plaintext: str, key : str):
        ciphertext = ""


        """
        the first letter in each rotor should match key before executing this function    
        
        """
        # Main loop to iterate through plaintext
        for letter in plaintext:
            """ 
            valueofLetter = char_to_value.get("A")
            value_c1 = cylinder1[valueofletter]
            value_c2 = cylinder2[value_c1]
            value_c3 = cylinder3[value_c2]
            cipher_char = value_to_char.get(value_c3)
            ciphertext += cipher_char
            rotate forward all cylinders + 1
            """

    # TODO decryption function

    """
    implementation details should be the opposite of encryption
    search for value in rotors starting from rotor 3 and use search position from
    previous rotor in the next (rotor 2, then rotor 1). Each rotor needs to be configured
    in the position after the encryption of all the characters.
    """



pt = "JAZZ"
# print(pt)
list_of_rotors= [rotor_1,rotor_2,rotor_3]
# Test Rotor Machine
# RotorMachine(list_of_rotors,"CAB")




