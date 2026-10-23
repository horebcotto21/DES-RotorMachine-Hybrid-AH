#Python 3.14
# need to create relationship between 3 arrays

import string
from collections import namedtuple
from random import randint

alpha_to_value = {char: i for i, char in enumerate(string.ascii_uppercase)}
value_to_alpha = {i: char for i, char in enumerate(string.ascii_uppercase)}

# mapping between alphabet and first cylinder and between the other cylinders

""" 
If RotorMachine is going to be used from another file (to use the two encryption algorithms consecutively) 
a class for the rotor machine may be needed
"""

# TODO Initial configuration of the 3 rotors numbers from 0-25 each with a unique order


#Example DO NOT USE
rotor_1 = ["A","J","I","Z","H"]
rotor_2 = ["C","X","E","P","S"]
rotor_3 = ["Q","F","S","H","R"]

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
use value from that inedx in list of second rotor as index for third rotor
use value from third rotor and look for what letter it belongs to
"""
# @Andrea
# TODO Rotor Class initilized with the rotors defined previously and key



# @Horeb
# TODO function to configure each rotor with three letter key as parameter



# @Horeb
# TODO rotor forward(last element to top) and reverse (top element to bottom) inside rotor class
#example of rotation operation, not correct direction for forward
def rotate(rotor : list):
        rotor = rotor[:1] + rotor[:1]
        return rotor

# @Andrea
# TODO encrypt function uses loop to iterate through plaintext, and encrypt one letter at a time
def encrypt(plaintext, key : str):
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

# encrypt(pt,"ABC")



