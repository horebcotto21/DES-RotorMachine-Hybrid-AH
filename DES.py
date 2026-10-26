#Python 3.14

# Data -----------------------------------------------
# Initial Permutation Table
IP_table = [    58, 50, 42, 34, 26, 18, 10, 2,
				60, 52, 44, 36, 28, 20, 12, 4,
				62, 54, 46, 38, 30, 22, 14, 6,
				64, 56, 48, 40, 32, 24, 16, 8,
				57, 49, 41, 33, 25, 17,  9, 1,
				59, 51, 43, 35, 27, 19, 11, 3,
				61, 53, 45, 37, 29, 21, 13, 5,
				63, 55, 47, 39, 31, 23, 15, 7]

PC1_table = [   57, 49, 41, 33, 25, 17,  9,
                1,  58, 50, 42, 34, 26, 18,
                10, 2,  59, 51, 43, 35, 27,
                19, 11, 3,  60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7,  62, 54, 46, 38, 30, 22,
                14, 6,  61, 53, 45, 37, 29,
                21, 13,  5, 28, 20, 12,  4]

PC2_table = [   14, 17, 11, 24,  1,  5,
                 3, 28, 15,  6, 21, 10,
                23, 19, 12,  4, 26,  8,
                16,  7, 27, 20, 13,  2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]
"""
For each round bits of key are shifted
1-bit shift rounds: Rounds 1, 2, 9, and 16
2-bit shift rounds: Rounds 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, and 15
"""
shifts_per_round = [ 1, 1, 2, 2,
                     2, 2, 2, 2,
                     1, 2, 2, 2,
                     2, 2, 2, 1]

# TODO S-boxes
#-----------------------------------

# Helper Functions------------------
def hex_to_bin(hexadecimal: str)-> str:
    # could be with a dictionary mapping each hexadecimal character to binary equivalent
    return bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4)

# Core cryptographic techniques--------
""" Permutation Function
Parameters:
    block : str - string that will be permutated using a table from Data section
    table : list - a sequence of numbers used for permutation
    bits : int - how many bits does the result need to have
Returns:
    permutated_block : str - block that passed through permutation table 
"""
def permutation(block : str,table: list,bits):
    permutated_block = ""
    for i in range(0,bits):
        permutated_block = permutated_block + block[table[i]-1]
    return permutated_block


# TODO Substitution function using eight S‑boxes

#----------------------------------------


"""DES Class
Parameter:

"""
class DES:
    def __init__(self, key :str):
        # Step 1 generate subkeys
        self.subkeys_list = Key(key).subkeys()


    def __pt_padding(self,text: str):
        # parse spaces/ should they be removed or used as part of the text to be encrypted?
        parsed_text = text.replace(" ", "")
        #encode so we can pad plaintext
        encoded_pt = parsed_text.encode("utf-8")
        # pad pt if needed
        bytes_needed = len(encoded_pt)
        # inputs in project are not longer than 8 bytes should add case later
        if len(encoded_pt) < 8:
            encoded_pt = encoded_pt.ljust(8, b'\x00')
        padded_pt = encoded_pt.hex()
        # blocks: list = [encoded_pt[i: i + 16] for i in range(0, len(padded_hex_pt), 8)]
        # to binary

        return hex_to_bin(padded_pt)

    """
    16 rounds of encryption
    divide plaintext into two 64 Bit size blocks main/final key 56 bits long

    key[i] where i is current round is a permutation or a split of original 56 length key after removing parity bits

    alternate substitution and permutation techniques
    """
    def __feistel_rounds(self,hex_string: str,subkeys: list):
        # Initial permutation
        block = permutation(hex_string, IP_table, 64)

        # Split block in half
        LE = block[0:16]
        RE = block[16:64]
        """ 
        right block is expanded up to 48 bits

        applied a permutation or a substitution technique (start with permutation) using a 
        permutation/slice of 56 bit key generated, they should alternate. Use mod 2 == 0 to know when round is even
        """

        for i in range(16):
            # ask for key for this round = key[i]
            # apply permutation or substitution using key[i] starting with permutation on round 1
            # right side for next round becomes xor operation of the result string from the right after function and Left side of plaintext
            # left side for next round will be original right( before function)

            LE = RE
            RE = LE

    def test(self,plaintext: str):
        block = self.__pt_padding(plaintext)
        print(permutation(hex_to_bin(block),IP_table,64))
        # self.__feistel_rounds(block,self.subkeys_list)


    def encrypt(self,plaintext :str):
        # Step 2 permutation of plaintext using initial 8x8 64 bit permutation table
        permutated_pt = self.__pt_padding(plaintext)
        # Step 3 Feistel Rounds
        self.__feistel_rounds(permutated_pt,self.subkeys_list)


    def decrypt(self,ciphertext :str):
        # Step 2 if encrypted with this algorithm should already be appropriate length
        permutated_pt = self.__pt_padding(ciphertext)
        # Step 3 Feistel Rounds


""" Key class
Parameters:
    key : str - 16 character string

class validates key, by checking there isn't a letter not in hexadecimal
or not exactly 16 characters in length. uses default key any of these checks fail. 
"""
class Key:
    def __init__(self, key: str):
        # validate
        if self.validate(key):
            self.key = key
        else:
            # default key
            print("key was not valid, using default key")
            self.key = "1337BACEF18CC54D"

    def __shift_subkey(self,subkey: str,amount: int):
        shift = ""
        for i in range(0,amount):
            for j in range(0,len(subkey)):
                shift = shift + subkey[j]
            shift = shift + subkey[0]
            subkey = shift
            shift = ""
        return subkey

    def validate(self,key) -> bool:
        if len(key) != 16:
            return False
        try:
            int(key, 16)
        except ValueError:
            return False
        return True

    def subkeys(self) -> list:
        # create keys for the 16 rounds of encryption/dedcryption

        # convert key to binary
        bin_key = hex_to_bin(self.key)
        # remove parity bits
        no_parity_key = permutation(bin_key, PC1_table, 56)
        # print(no_parity_key, len(no_parity_key))
        half = int(len(no_parity_key) / 2)
        # split in half
        left = no_parity_key[0:half]
        right = no_parity_key[half:56]
        subkeys_list = []
        for i in range(0,16):
            # shift operations based on round
            left = self.__shift_subkey(left,i)
            right = self.__shift_subkey(right,i)
            combine = left + right
            subkey = permutation(combine, PC2_table, 48)
            subkeys_list.append(subkey)
        return subkeys_list

# Key generation test-------
# valid_key = "133759BBC356F11D"
# invalid_key = "23F"
# subkeys = Key(valid_key).subkeys()
# count = 1
# for s in subkeys:
#     print(s,count)
#     count += 1

# Padding and IP test-----------
# DES("AABB09182736CCDD").test("HELLO")


