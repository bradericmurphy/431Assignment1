import sys, re, io, string



emailPattern = r"(^[\w.+-]+@[\w-]+\.[\w-.]+$)"

mailFrom = "^MAIL[\s\t]+FROM:"

for line in sys.stdin:



    #print (line.rstrip("\r\n"))
    #fromStr = line.split(' ', 1)[0]
    #print(fromStr)



#Then do the loop

#for pattern in in:
#    print (pattern.rstrip("\r\n"))

def checkIfNum(character):
    numpattern = "\d"
    character.match(numpattern)
    #Not Finished??

def checkIfSpecial(character):
    if (val == 60 | val == 62 | val == 40 | val == 41 | val == 91 | val == 93 | val == 92 | val == 46 | val == 44 | val == 59 | val == 58 | val == 64 | val == 34):
        #return boolean

def checkIfNonSpecial(character)
    val = ord(character)
    if ((val < 128) & (val == 60 | val == 62 | val == 40 | val == 41 | val == 91 | val == 93 | val == 92 | val == 46 | val == 44 | val == 59 | val == 58 | val == 64 | val == 34 | val == 32)):
        #return boolean

def sp(character):
    val = ord(character)
    if (val = 32 | val = 9):
        #return boolean

def checkIfA():
    apattern = "[A-Za-z]"
    character.match(apattern)
    #Not Finished


