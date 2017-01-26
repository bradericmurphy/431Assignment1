import sys, re, io, string



mailFrom = "^MAIL[\s]+FROM:"
mailFromPattern = re.compile(mailFrom)

num = "\d"
numPattern = re.compile(num)

whitespace = "[\t\s\r\f\v]"
whitespacePattern = re.compile(whitespace)

special = "[][<>(),.;:@\\\\'\"']"
specialPattern = re.compile(special)

a = "[A-Za-z]"
aPattern = re.compile(a)

def d(character):
    return bool(character.match(numPattern))

def special(thisstring):
    return bool(specialPattern.search(thisstring))
    #val = ord(character)
    #return bool(val == 60 | val == 62 | val == 40 | val == 41 | val == 91 | val == 93 | val == 92 | val == 46 | val == 44 | val == 59 | val == 58 | val == 64 | val == 34)

def c(character):
    val = ord(character)
    return bool((val < 128) & (val != 60 | val != 62 | val != 40 | val != 41 | val != 91 | val != 93 | val != 92 | val != 46 | val != 44 | val != 59 | val != 58 | val != 64 | val != 34 | val != 32))

def sp(thisstring):
    return bool(whitespacePattern.search(thisstring))

def a(character):
    return bool(aPattern.match(character))

def charCheck(character):
    return c(character)

def crlf(character):
    newlinepattern = "\n"
    return bool(character.match(newlinepattern))

def letDig(character):
    return bool(a(character) | d(character))

#def letdigstr(character, charCounter):
 #   if (bool(a(character)))

#def MailFromCmd():

for line in sys.stdin:
    print(line.rstrip("\n"))
    strList = line.split(':', 1)
    mailFromString = strList[0]+':'
    if (not (bool(mailFromPattern.match(mailFromString)))):
        print("ERROR -- mail-from-cmd")
        continue


    restOfString = strList[1].lstrip()
    if ord(restOfString[0]) != 60:
        print("ERROR -- path")
        continue

    strList = restOfString.split('@', 1)
    strin = strList[0]
    remainingStr = '@' + strList[1]
    strin = strin.lstrip('<')
    stopHereCheck = sp(strin)
    if special(strin):
        stopHereCheck = True

    if stopHereCheck == True:
        print("ERROR -- local-part")
       #print(strin + str(len(strin)))#used for testing
        continue








    #print (line.rstrip("\r\n"))
    #fromStr = line.split(' ', 1)[0]
    #print(fromStr)


