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

# Positions for plaintext after first permutation
text_permutation =[
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

# Straight Permutaion Table
straight_permutation = [
        16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25 ]

# S-box Table
s_box =  [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],

        [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],

        [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],

        [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],

        [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],

        [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],

        [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

# Final Permutaion Table
final_permutation = [ 40, 8, 48, 16, 56, 24, 64, 32,
               39, 7, 47, 15, 55, 23, 63, 31,
               38, 6, 46, 14, 54, 22, 62, 30,
               37, 5, 45, 13, 53, 21, 61, 29,
               36, 4, 44, 12, 52, 20, 60, 28,
               35, 3, 43, 11, 51, 19, 59, 27,
               34, 2, 42, 10, 50, 18, 58, 26,
               33, 1, 41, 9, 49, 17, 57, 25 ]

# Table containing the number of bitwise shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

class DES:
    # Hexadecimal to binary
    def hex_to_bin(self, hex):
        hex_table = {
            '0' : "0000",
            '1' : "0001",
            '2' : "0010",
            '3' : "0011",
            '4' : "0100",
            '5' : "0101",
            '6' : "0110",
            '7' : "0111",
            '8' : "1000",
            '9' : "1001",
            'A' : "1010",
            'B' : "1011",
            'C' : "1100",
            'D' : "1101",
            'E' : "1110",
            'F' : "1111"
        }

        binary = ""
        # loop through each hex character convert hex to binary
        for i in range(len(hex)):
            binary = binary + hex_table[hex[i]]
        return binary

    # Binary to Hexadecimal
    def bin_to_hex(self, bin):
        binary_table = {
            "0000" : '0',
            "0001" : '1',
            "0010" : '2',
            "0011" : '3',
            "0100" : '4',
            "0101" : '5',
            "0110" : '6',
            "0111" : '7',
            "1000" : '8',
            "1001" : '9',
            "1010" : 'A',
            "1011" : 'B',
            "1100" : 'C',
            "1101" : 'D',
            "1110" : 'E',
            "1111" : 'F'
        }

        hex = ""
        # Loop by 4 characters instead of 1 for binary to hexadecimal conversion
        for i in range(0, len(bin), 4):
            bits = ""
            bits = bits + bin[i]
            bits = bits + bin[i + 1]
            bits = bits + bin[i + 2]
            bits = bits + bin[i + 3]
            hex = hex + binary_table[bits]

        return hex

    # Binary to decimal
    def bin_to_dec(self, bin):
        decimal = i = 0
        while(bin != 0):
            dec = bin % 10
            decimal = decimal + dec * pow(2, i)
            bin = bin // 10
            i += 1

        return decimal

    # Decimal to binary
    def dec_to_bin(self, dec):
        binary = bin(dec).replace("0b", "")
        # pad zeros if number of bits isn't a multiple of 4
        if(len(binary) % 4 != 0):
            pad = int(len(binary) /4)
            pad = (4 * (pad + 1)) - len(binary)
            for i in range(0, pad):
                binary = "0" + binary

        return binary

    # shift the bits left by n
    def shift_left(self, bits, n):
        shift = ""
        for i in range(n):
            for j in range(1, len(bits)):
                shift = shift + bits[j]
            shift = shift + bits[0]
            bits = shift
            shift = ""

        return bits

    # calculate xor between two binary strings
    def xor(self, a, b):
        result = ""
        for i in range(len(a)):
            if a[i] == b[i]:
                result = result + "0"
            else:
                result = result + "1"

        return result

    def permutation(self, pre_perm, table, length):
        perm = ""
        for i in range(0, length):
            perm = perm + pre_perm[table[i] - 1]
        return perm

    # Encryption algorithim for DES
    def encrypt(self, plaintext, key):
        # Key transformation, in binary
        key = hex_to_bin(key)
        key = self.permutation(key, key_permutation, 56)

        # split the key into two halves
        left = key[0:28]
        right = key[28:56]

        # contains the keys after bit shifts and key compression
        keys = []

        # Create 16 rounds of keys for encryption/decryption
        for i in range(0, 16):
            # Shift the key bits left based on bits in shift table
            left = self.shift_left(left, shift_table[i])
            right = self.shift_left(right, shift_table[i])

            # Combine left and right key after bitwise shift left
            new_key = str(left + right)

            # Compress key to 48 bits
            new_key = self.permutation(new_key, key_compression, 48)

            keys.append(new_key)

        # Text transformation, needs to be binary
        plaintext = self.hex_to_bin(plaintext)
        text = self.permutation(plaintext, text_permutation, 64)

        # split the text into two halves
        left = text[0:32]
        right = text [32:64]


        for i in range(0, 16):
            # expansion Permutation, 32 bits to 48
            right_expanded = self.permutation(right, expansion_permutation, 48)

            # XOR expanded right text and key[i]
            x = self.xor(right_expanded, keys[i])

            # S-box Permutation
            s_str = ""
            for j in range(0,8):
                row = self.bin_to_dec(int(x[j * 6] + x[j * 6 + 5]))
                col = self.bin_to_dec(int(x[j * 6 + 1] + x[j * 6 + 2] + x[j * 6 + 3] + x[j * 6 + 4]))
                s = s_box[j][row][col]
                s_str = s_str + self.dec_to_bin(s)

            # Straight Permutation results in 32 bits for xor
            s_str = self.permutation(s_str, straight_permutation, 32)

            # xor left half of plaintext s_str and swap left and right halves
            left_xor = self.xor(left, s_str)
            left = left_xor

            if(i != 15):
                left, right = right, left

        # rejoin halves and a final permutation is done on the combined block
        final = left + right
        cipher = self.permutation(final, final_permutation, 64)
        return self.bin_to_hex(cipher)

    # Decryption algorithim for DES
    def decrypt(self, ciphertext, key):
        # Key transformation, in binary
        key = hex_to_bin(key)
        key = self.permutation(key, key_permutation, 56)

        # split the key into two halves
        left = key[0:28]
        right = key[28:56]

        # contains the keys after bit shifts and key compression
        keys = []

        # Create 16 rounds of keys for encryption/decryption
        for i in range(0, 16):
            # Shift the key bits left based on bits in shift table
            left = self.shift_left(left, shift_table[i])
            right = self.shift_left(right, shift_table[i])

            # Combine left and right key after bitwise shift left
            new_key = str(left + right)

            # Compress key to 48 bits
            new_key = self.permutation(new_key, key_compression, 48)

            keys.append(new_key)
        # reverse keys for decryption
        keys = keys[::-1]

        # Text transformation, needs to be binary
        ciphertext = self.hex_to_bin(ciphertext)
        text = self.permutation(ciphertext, text_permutation, 64)

        # split the text into two halves
        left = text[0:32]
        right = text [32:64]


        for i in range(0, 16):
            # expansion Permutation, 32 bits to 48
            right_expanded = self.permutation(right, expansion_permutation, 48)

            # XOR expanded right text and key[i]
            x = self.xor(right_expanded, keys[i])

            # S-box Permutation
            s_str = ""
            for j in range(0,8):
                row = self.bin_to_dec(int(x[j * 6] + x[j * 6 + 5]))
                col = self.bin_to_dec(int(x[j * 6 + 1] + x[j * 6 + 2] + x[j * 6 + 3] + x[j * 6 + 4]))
                s = s_box[j][row][col]
                s_str = s_str + self.dec_to_bin(s)

            # Straight Permutation results in 32 bits for xor
            s_str = self.permutation(s_str, straight_permutation, 32)

            # xor left half of ciphertext s_str and swap left and right halves
            left_xor = self.xor(left, s_str)
            left = left_xor

            if(i != 15):
                left, right = right, left

        #  havles are rejoined and final permutation is done on the combined block
        final = left + right
        cipher = self.permutation(final, final_permutation, 64)
        return self.bin_to_hex(cipher)
