import sys, re, io, string
charCounter = 0


emailPattern = r"(^[\w.+-]+@[\w-]+\.[\w-.]+$)"

mailFromPattern = "^MAIL[\s\t]+FROM:"

for line in sys.stdin:
print(line)
strList = line.split(':', 1)
mailFromString = strList[0]+':'

if (!(bool(mailFromString.match(mailFromPattern)))):
    print("ERROR -- mail-from-cmd")



    #print (line.rstrip("\r\n"))
    #fromStr = line.split(' ', 1)[0]
    #print(fromStr)



#Then do the loop

#for pattern in in:
#    print (pattern.rstrip("\r\n"))


def d(character):
    numpattern = "\d"
    return bool(character.match(numpattern))


def special(character):
    return (val == 60 | val == 62 | val == 40 | val == 41 | val == 91 | val == 93 | val == 92 | val == 46 | val == 44 | val == 59 | val == 58 | val == 64 | val == 34)


def c(character)
    val = ord(character)
    return ((val < 128) & (val != 60 | val != 62 | val != 40 | val != 41 | val != 91 | val != 93 | val != 92 | val != 46 | val != 44 | val != 59 | val != 58 | val != 64 | val != 34 | val != 32))

def sp(character):
    val = ord(character)
    return (val == 32 | val == 9)

def a(character):
    apattern = "[A-Za-z]"
    return bool(character.match(apattern))

def charCheck(character):
    return c(character)

def crlf(character):
    newlinepattern = "\n"
    return bool(character.match(newlinepattern))

def letDig(character):
    return bool(a(character) | d(character))

def letdigstr(character, charCounter):
    if (bool(a(character))):

def MailFromCmd()