#Python 3.14

# TODO Step 1 permutation of plaintext using initial 8x8 64 bit permutation table
""""
Initial Permutation Table

58	50	42	34	26	18	10	2
60	52	44	36	28	20	12	4
62	54	46	38	30	22	14	6
64	56	48	40	32	24	16	8
57	49	41	33	25	17	9	1
59	51	43	35	27	19	11	3
61	53	45	37	29	21	13	5
63	55	47	39	31	23	15	7

"""

# TODO Step 2 initial process of 64-bit key
"""
Need to take out 8 parity bits
Using PC-1 table
Left half	|57 49 41 33 25 17 9  1	|58 50 42 34 26 18 10 2	|59 51 43 35 27 19 11 3 |60 52 44 36                       
Right half	|63 55 47 39 31 23 15 7	|62 54 46 38 30 22 14 6	|61 53 45 37 29 21 13 5 |28 20 12 4

Split remaining 56 bits in half 28 bits
"""

# TODO function to process 2 halves each round
"""
For each round bits of key are shifted
1-bit shift rounds: Rounds 1, 2, 9, and 16
2-bit shift rounds: Rounds 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, and 15
shits made on keys are cumulative, next round will use previous rounds shifted halves

combine halves into 56-bit string and drop 8 bits to create 48-bit key for this round  
PC-2 Table
14  17  11  24   1   5
3   28  15   6  21  10
23  19  12   4  26   8
16   7  27  20  13   2
41  52  31  37  47  55
30  40  51  45  33  48
44  49  39  56  34  53
46  42  50  36  29  32

and use the remaining 56 to create 16 unique 48 bit keys for each round

"""

# TODO Feistel structure
"""
16 rounds of encryption
divide plaintext into two 64 Bit size blocks main/final key 56 bits long

key[i] where i is current round is a permutation or a split of original 56 length key after removing parity bits

alternate substitution and permutation techniques
"""

# LOOP range 16 O(16)-> O(1)
# ask for key for this round = key[i]
# apply permutation or substitution using key[i] starting with permutation on round 1
# right side for next round becomes xor operation of the result string from the right after function and Left side of plaintext
# left side for next round will be original right( before function)

""" 
right block is expanded up to 48 bits

applied a permutation or a substitution technique (start with permutation) using a 
permutation/slice of 56 bit key generated, they should alternate. Use mod 2 == 0 to know when round is even
"""



# TODO Permutation function using a P‑box


# TODO Substitution function using eight S‑boxes