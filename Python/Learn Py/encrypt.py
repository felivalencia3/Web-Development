import re
import string
def Encrypt(str):
    lower = str.lower()
    thelist =list(lower)
    alphabet = list(string.ascii_lowercase)
    if(thelist.count("z")==1):
        thelist[thelist.index("z")] = "c"
    if (thelist.count("y")==1):
        thelist[thelist.index("y")] = "b"
    if (thelist.count("x")==1):
        thelist[thelist.index("x")] = "a"
    if (thelist.count("x")==0 and thelist.count("y")==0 and thelist.count("z")==0):
        for chara in thelist:
            indexer = thelist.index(chara)
            chars = thelist[indexer]
            charsindexfound = alphabet.index(chara)+3
            final1 = alphabet[charsindexfound]
            list2 = list(final1)
            for newchar in list2:
                if (list2.count("e") >= 1):
                    eindex = list2.index("e")
                    list2[eindex] = "2"
                elif (list2.count("i") >= 1):
                    iindex = list2.index("i")
                    list2[iindex] = "3"
                elif (list2.count("o") >= 1):
                    oindex = list2.index("o")
                    list2[oindex] = "4"
                elif (list2.count("u") >= 1):
                    uindex = list2.index("u")
                    list2[uindex] = "5"
                #final = " ".join(list2)
                #final.replace("\n", " ")
                #print(final)
                for i in range(len(list2)):
                    print(list2[i], end="")
Encrypt(input("Enter a String to be Encrypted:\n"))
