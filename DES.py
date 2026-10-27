#Python 3.14
from turtledemo import planet_and_moon

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

#Straight Permutation
SP_table = [16,  7, 20, 21,
            29, 12, 28, 17,
             1, 15, 23, 26,
             5, 18, 31, 10,
             2,  8, 24, 14,
            32, 27,  3,  9,
            19, 13, 30,  6,
            22, 11,  4, 25]

FP_table = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41,  9, 49, 17, 57, 25]
"""
For each round bits of key are shifted
1-bit shift rounds: Rounds 1, 2, 9, and 16
2-bit shift rounds: Rounds 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, and 15
"""
shifts_per_round = [ 1, 1, 2, 2,
                     2, 2, 2, 2,
                     1, 2, 2, 2,
                     2, 2, 2, 1]

# D-Box
d_box = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1]

# S-boxes
s1 = [  [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
s2 = [  [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
s3 = [  [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
s4 = [  [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
s5 = [  [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
s6 = [  [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
s7 = [  [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
s8 = [  [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

s_boxes = [s1,s2,s3,s4,s5,s6,s7,s8]
#-----------------------------------

# Helper Functions------------------
def hex_to_bin(hexadecimal: str):
    # could be with a dictionary mapping each hexadecimal character to binary equivalent
    return bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4)

def bin2hex(s):
    mp = {"0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]


    return hex


def bin_to_dec(binary: str):
    return int(binary,2)

# doesnt work
def dec_to_bin(decimal: int):
    return bin(int(decimal, 16))[2:].zfill(len(decimal) * 4).encode()

#from geeksforgeeks Author: Aditya Jain
def dec2bin(num):
    """Convert a decimal number to binary sequence

    :param num: an integer
    :return: a string with a binary sequence
    """
    res = bin(num).replace("0b", "")
    if len(res) % 4 != 0:
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def xor_operation(bin1: str, bin2: str) -> str:
    """Performs XOR operation on two binary strings
    if both have the same value (1,1) or (0,0) in position i becomes 0
    if they have different values (1,0) or (0,1) in position i becomes 1

    :param bin1: a string with a binary sequence
    :param bin2: a string with a binary sequence
    :return: a string with a binary sequence
    """
    xor = ""
    # a and b must have same length
    for i in range(len(bin1)):
        if bin1[i] == bin2[i]:
            xor = xor + "0"
        else:
            xor = xor + "1"
    return xor


# Core cryptographic techniques--------
def permutation(block : str,table: list,bits):
    """ Applies diffusion to the binary sequence using specified table

    :param block: string that will be permutated using a table from Data section
    :param table: a sequence of numbers used for permutation
    :param bits: how many bits does the result need to have
    :return: block that passed through permutation table
    """
    # block is a binary string
    permutated_block = ""
    for i in range(0,bits):
        permutated_block = permutated_block + block[table[i]-1]
    return permutated_block


def substitution(block : str):
    """ Substitution function using eight S‑boxes
    Applies confusion to input

    :param block: a string containing a binary sequence
    :return:
    """
    subs_text = ""
    for sbox in range(0,8):
        row = bin_to_dec(block[sbox * 6] + block[sbox * 6 + 5] )
        col = bin_to_dec(block[sbox * 6 + 1] + block[sbox * 6 + 2] + block[sbox*6 + 3] + block[sbox*6 + 4]  )

        val = s_boxes[sbox][row][col]
        subs_text = subs_text + dec2bin(val)

    return subs_text

#----------------------------------------

class DES:
    def __init__(self, key :str):
        # Step 1 generate subkeys
        self.subkeys_list = Key(key).subkeys()
        self.inv_subkeys_list = self.subkeys_list[::-1]


    def __pt_padding(self,text: str):
        """ Pads plaintext if it does not meet size requirements (too small)

        :param text: string to be padded
        :return: padded string in hex format
        """
        # parse spaces/ should they be removed or used as part of the text to be encrypted?
        # parsed_text = text.replace(" ", "")
        #encode so we can pad plaintext
        encoded_pt = text.encode("utf-8")
        # pad pt if needed
        bytes_needed = len(encoded_pt)
        # inputs in project are not longer than 8 bytes should add case later
        if len(encoded_pt) < 8:
            encoded_pt = encoded_pt.ljust(8, b'\x00')
        padded_pt = encoded_pt.hex()
        # for pt longer than 8 bytes

        # to binary

        return padded_pt

    def __unpadding(self,text : str):
        """Unpads text in parameter (removes trailing nulls)

        :param text: hex string to be unpadded
        :return: unpadded string in hex format
        """
        while text.endswith("00"):
            text = text[:-2]
        return text



    def __feistel_rounds(self,LE, RE,encryption: bool):
        """ Perform DES algorithm
        16 rounds of encryption

        :param LE - left side of block
        :param RE - right side of block
        :param encryption - whether encryption or decryption is going to be executed
        :return - returns binary version of encryption
        """
        for i in range(16):
            # Round 1
            # expand right side with D-box to 48-bits
            expanded_RE = permutation(RE, d_box, 48)

            # XOR with key for this round
            if encryption:
                xored = xor_operation(expanded_RE, self.subkeys_list[i])
            else:
                xored = xor_operation(expanded_RE, self.inv_subkeys_list[i])
            # substitution through all 8 sboxes
            sboxed = substitution(xored)

            # Straight permutation
            sp = permutation(sboxed, SP_table, 32)
            # XOR left with result of function
            processed = xor_operation(LE, sp)
            LE = processed

            # last round is different
            if i != 15:
                #swap LE and RE
                LE, RE = RE, LE

        combine_halves = LE + RE
        return combine_halves


    def encrypt(self,plaintext :str):
        """Calls padding function,applies initial permutation, splits block in two
        If plaintext is bigger than 8 bytes divides into 8 byte sized blocks and recursively calls encrypt method

        :param plaintext: text to be encrypted
        :return: string in hex format
        """
        #Step 1 prepare plaintext
        # pad text returns in binary
        if len(plaintext) > 8:
            blocks: list = [plaintext[i: i + 8] for i in range(0, len(plaintext), 8)]
            ciphertext : str = ""
            for block in blocks:
                temp = self.encrypt(block)
                ciphertext = ciphertext + temp
            return ciphertext
        # Step 2
        # Pad
        padded_pt = self.__pt_padding(plaintext)
        # Initial Permutation of pt
        ip_pt = permutation(hex_to_bin(padded_pt), IP_table, 64)
        # Split into blocks of the same size
        LE = ip_pt[0:32]
        RE = ip_pt[32:64]
        # Step 3 Feistel Rounds
        final_combine = self.__feistel_rounds(LE,RE,True)
        ciphertext = permutation(final_combine, FP_table,64)
        return bin2hex(ciphertext)


    def decrypt(self,ciphertext :str):
        """ Applies initial permutation to ciphertext, splits block in two
        If plaintext is bigger than 8 bytes divides into 8 byte sized blocks and recursively calls decrypt method

        :param ciphertext: string in hex format
        :return: string in ASCII format
        """
        # assume ciphertext is in hexadecimal format
        # Step 2 if encrypted with this algorithm should already be appropriate length
        if len(ciphertext) > 16:
            blocks: list = [ciphertext[i: i + 16] for i in range(0, len(ciphertext), 16)]
            plaintext : str = ""
            for block in blocks:
                temp = self.decrypt(block)
                plaintext = plaintext + temp
            return plaintext
        # no padding necessary is in hex format
        # padded_pt = self.__pt_padding(ciphertext)
        ip_pt = permutation(hex_to_bin(ciphertext), IP_table, 64)
        LE = ip_pt[0:32]
        RE = ip_pt[32:64]
        # Step 3 Feistel Rounds
        final_combine = self.__feistel_rounds(LE,RE,False)
        plaintext = permutation(final_combine, FP_table,64)
        stripped = bytearray.fromhex(self.__unpadding(bin2hex(plaintext))).decode()

        return stripped



class Key:
    def __init__(self, key: str):
        """ Generates subkeys

        :param key: 64-bit hex key
        """
        # validate
        if self.validate(key):
            self.key = key
        else:
            # default key
            print("key was not valid, using default key")
            self.key = "1337BACEF18CC54D"

    def __shift_subkey(self,subkey: str,amount: int):
        """Shifts left the subkey a number of times, specified by amount parameter

        :param subkey: no parity bit 56-bit key
        :param amount: how many left shifts are needed
        :return: a binary sequence in a string
        """
        shift = ""
        for i in range(0,amount):
            for j in range(1,len(subkey)):
                shift = shift + subkey[j]
            shift = shift + subkey[0]
            subkey = shift
            shift = ""
        return subkey

    def validate(self,key) -> bool:
        """ Checks that the key is right length and contains no non-hex value

        :param key: original 64-bit hex key
        :return: boolean
        """
        if len(key) != 16:
            return False
        try:
            int(key, 16)
        except ValueError:
            return False
        return True

    def subkeys(self) -> list:
        """ Create keys for the 16 rounds of encryption/decryption

        :return: list of subkeys in order for encryption
        """
        # convert key to binary
        bin_key = hex_to_bin(self.key)
        # remove parity bits
        no_parity_key = permutation(bin_key, PC1_table, 56)
        # split in half
        left = no_parity_key[0:28]
        right = no_parity_key[28:56]
        subkeys_list = []
        for i in range(0,16):
            # shift operations based on round
            left = self.__shift_subkey(left,shifts_per_round[i])
            right = self.__shift_subkey(right,shifts_per_round[i])
            combine = left + right
            subkey = permutation(combine, PC2_table, 48)
            subkeys_list.append(subkey)
        return subkeys_list

