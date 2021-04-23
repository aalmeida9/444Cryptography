class Cryptography:
    myOriginalMessage = "test";
    myCypherType = 1;
    alphabetCount = 26;
    def __init__(self, myMessage, myCypher):
        self.myOriginalMessage = myMessage;
        self.myCypherType = myCypher;



    def encryptCaesar(self, myKey):
        myMessage = "";

        for x in self.myOriginalMessage:
            # check if upper or lower case and create the numeric representation accordingly
            if x.isupper():
                a = 65
            else:
                a = 97

            #create offset for each letter in the original message
            letterAsNum = ord(x) - a
            newIndex = (letterAsNum + myKey) % self.alphabetCount
            c = newIndex + a
            newChar = chr(c)
            myMessage += newChar

        print("your encrypted message is", myMessage)

    def decryptCaesar(self, myKey):
        myMessage = "";

        for x in self.myOriginalMessage:
            # check if upper or lower case and create the numeric representation accordingly
            if x.isupper():
                a = 65
            else:
                a = 97

            # create offset for each letter in the original message
            letterAsNum = ord(x) - a
            newIndex = (letterAsNum - myKey) % self.alphabetCount
            c = newIndex + a
            newChar = chr(c)
            myMessage += newChar

        print("your decrypted message is", myMessage)

a = Cryptography("HeLlO", 1);

a.encryptCaesar(2);

b = Cryptography("JgNnQ", 1);
b.decryptCaesar(2);