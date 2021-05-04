# ceasar cipher has a keyspace of 26 loop through the key space and
# keep track of the key that has the most matches to the dictionary
# for each letter in alphabet check if the caesar cypher
# for each "decrypted" text compare it to the dictionary
import csv
import time
from Ceaser import Cryptography
from DES import DES

with open('ourDictionary.txt', 'r') as d:
    dictionary = d.readlines()

dictionaryList = []
for x in dictionary:
    dictionaryList.append(x.strip())

# read the file apnd put it in the array
# first column   = sender
# second column  = receiver
# third column   = type of encryption (CS, DES, 3DES)
# fourth column  = encrypted message
#encryptedMessage = [];
encryptedText = ""
caesar = Cryptography(encryptedText, 1);
output = open('output.txt', 'w')

with open('input.txt') as csvFile:
    csvFileReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in csvFileReader:
        print(" ")
        print("Decrypting message {}, from {} to {} with encryption alogirthm {}".format(row[3].strip(), row[0], row[1], row[2]))
        if(row[2] == " CS"):
            caesarStartTime = time.time()   # start timer to see how long it takes to decrypt
            for x in range(1, 26):
                encryptedText = caesar.decryptCaesar(x, row[3].strip())
                for word in dictionaryList:
                    #word.encode('unicode-escape').decode()
                    if(encryptedText.lower() == word):
                        outputWord = encryptedText.lower()
                        print("Match found: {} with key: {}".format(word, x))
                        break # once you find a match stop looping through possible matches
            endTime = time.time()
            print("Average time to solve this instance: {}".format((endTime - caesarStartTime)/25))


        elif(row[2] == " DES"):   # do DES algorithm
            des = DES()

            DESStartTime = time.time() # start timer
            # birth year between 1935 and 1950
            # input contains sender, receiver, encryption used, ciphertext
            # key space is the combination of 5 repetitions of the hex birthyear and
            # an additional character (0-F)
            #loop through the possible birth year repetitions, start before first year
            year = 1934
            count = 0
            for i in range(16):
                key = ""
                year += 1
                year_bin = des.dec_to_bin(year)
                year_hex = des.bin_to_hex(year_bin)
                for x in range(5):
                    key += year_hex

                key += "A"
                hex = des.decrypt(row[3].strip(), key)

                byte_array = bytearray.fromhex(hex)

                try:
                    outputWord = byte_array.decode('ascii')
                    print("Match found: {} with key: {}".format(outputWord, key))
                    for word in dictionaryList:
                        if(outputWord.strip() == word.strip()):
                            outputWord = text.lower()
                            print("Match found: {} with key: {}".format(outputWord, key))
                            break # once you find a match stop looping through possible matches
                except:
                    pass

            DESEndTime = time.time()
            print("Average time to solve this instance: {}".format((DESEndTime - DESStartTime)/16))
        #output all data to output file
        try:
            output.write("{}, {}, {}, {}\n".format(row[0], row[1], row[2], outputWord))

        except:
            pass
output.close()
