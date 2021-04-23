# ceasar cipher has a keyspace of 26 loop through the key space and
# keep track of the key that has the most matches to the dictionary
# for each letter in alphabet check if the caesar cypher
# for each "decrypted" text compare it to the dictionary
import csv
from Ceaser import Cryptography

with open('ourDictionary.txt') as file:
    dictionary = file.readlines()

dictionaryList = []
for x in dictionary:
    dictionaryList.append(x.rstrip('\n'))

# read the file apnd put it in the array
# first column   = sender
# second column  = receiver
# third column   = type of encryption (CS, DES, 3DES)
# fourth column  = encrypted message
#encryptedMessage = [];
encryptedText = ""
caesar = Cryptography(encryptedText, 1);
with open('input.txt') as csvFile:
    csvFileReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in csvFileReader:
        #decrypt caesar decrypt DES here
        #encryptedMessage.append(row);
        for x in range(1, 26):
            encryptedText = caesar.decryptCaesar(x, row[3].strip())
            for word in dictionaryList:
                if(encryptedText.lower() == word):
                    print("dictionary word is", word, "with caesar cypher ", x)


# create the caesar cypher object

# for each possible caesar cipher value, print the offset and decrypt it

   # for y in range


# birth year between 1970 (7B2) and 1985 (7C1)
# input contains sender, receiver, encryption used, ciphertext
# key space is the combination of 5 repetitions of the hex birthyear and
# an additional character (0-F)
