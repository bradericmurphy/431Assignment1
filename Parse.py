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
    numpattern = r"\d"
    character.match(numpattern)
    #Not Finished??

def checkIfSpecial(character):
    specialcharpattern = r"[[]<>()\.,;:@]"
    #DOES NOT INCLUDE QUOTE MARKS

def checkIfNonSpecial(character)
    val = ord(character)
    if (val == 60 | val == 62 | val == 40 | val == 41 | val == 91 | val == 93 | val == 92 | val == 46 | val == 44 | val == 59 | val == 58 | val == 64 | val == 34):
        #return boolean

def sp(character):
    val = org(character)
    if (val = space)