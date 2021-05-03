from bitstring import BitArray
# Permutation tables

# Positions for initial key permutation, results in 56 bits in key
key_permutation = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 ]

# Positions for initial key permutation, results in 48 bits in key
key_compression =[
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32 ]

# Table containing the bitwise shift
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

# Positions for plaintext after first permutation
plaintext_permutation =[
                58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

# Positions for half of the plain text to incrase bits from 32 to 48
expansion_permutation =[
         32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]

class DES:
    def permutation(self, pre_perm, table, length):
        perm = ""
        for i in range(0, length):
            perm = perm + pre_perm[table[i] - 1]
        return perm

    # Can also be used to decrypt cipher text by reversing the keys
    def encrypt(self, plaintext, key):
        # Start DES
        # Key transformation, in binary
        key = self.permutation(key, key_permutation, 56)

        # split the key into two halves
        left = key[0:28]
        right = key[28:56]

        # contains the keys
        keys = []

        # Create 16 rounds of keys for encryption/decryption
        for i in range(0, 16):
            # Shift the key bits left based on bits in shift table
            print("Left: {} Right: {}".format(left, right))
            #left = (left << shift_table[i])
            #right = (right << shift_table[i])
            print("ShiftLeft: {} ShiftRight: {}".format(left, right))

            # Combine left and right key after bitwise shift left
            #new_key = str(left + right)

            # Compress key to 48 bits
            #new_key = self.permutation(new_key, key_compression, 48)

            #keys.append(new_key)

        # Text transformation, needs to be binary
        text = self.permutation(plaintext, plaintext_permutation, 64)

        # split the text into two halves
        left = text[0:32]
        right = text [32:64]
        # expansion Permutation, 32 bits to 48
        right = self.permutation(right, expansion_permutation, 48)

        #for i in range(0, 16):
            # XOR

            # S-box Permutation

            # P-box Permutation

            # XOR and swap

            # Initial Permutation function on plain text


        # Each half goes through 16 rounds of Encryption

        # shift the bits left by n

        # ultimately havles are rejoined and a final permutation is done on the combined block


# 16 character (hex) key/ciphertext (64 bits)
# discard every 8th bit of key so key is 56 bits
# Example code
pt = "123456ABCD132536"
pt = "0001001000110100010101101010101111001101000100110010010100110110"
key = "AABB09182736CCDD"

key = "1010101010111011000010010001100000100111001101101100110011011101"

des = DES()
des.encrypt(pt, key)

#print(key)
