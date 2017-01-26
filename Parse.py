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
    return bool(numPattern.match(character))

def special(thisstring):
    return bool(specialPattern.search(thisstring))

def c(character):
    val = ord(character)
    return bool((val < 128) & (val != 60 | val != 62 | val != 40 | val != 41 | val != 91 | val != 93 | val != 92 | val != 46 | val != 44 | val != 59 | val != 58 | val != 64 | val != 34 | val != 32))

def sp(thisstring):
    return bool(whitespacePattern.search(thisstring))

def a(thisstring):
    return bool(aPattern.match(thisstring))

def charCheck(character):
    return c(character)

def crlf(character):
    newlinepattern = "\n"
    return bool(character.match(newlinepattern))

def letDig(character):
    return bool(a(character) | d(character))

for line in sys.stdin:
    print(line.rstrip("\n"))
    strList = line.split(':', 1)
    mailFromString = strList[0]+':'
    if (not (bool(mailFromPattern.match(mailFromString)))):
        print("ERROR -- mail-from-cmd")
        continue


    restOfString = strList[1].lstrip()
    if restOfString[0] != '<':
        print("ERROR -- path")
        continue

    strList = restOfString.split('@', 1)
    atCheck = restOfString.split('@')

    strin = strList[0]


    #Workaround Check
    if len(atCheck) != 2:
        print("ERROR -- mailbox")
        continue

    remainingStr = '@' + strList[1]
    strin = strin.lstrip('<')

    stopHereCheck = sp(strin)
    if special(strin):
        stopHereCheck = True

    if stopHereCheck == True:
        print("ERROR -- local-part")
        continue

    if remainingStr[0] != '@':
        print("ERROR -- mailbox")
        continue

    domainOn = remainingStr.lstrip('@')
    strList = domainOn.split('.')
    lastStr = strList[len(strList) - 1]


    keepGoing = True
    for i in range (0, len(strList), 1):

        domain = strList[i]
        testDomain = domain.split()

        if len(testDomain) > 0:
            if sp(testDomain[0]):
                print("ERROR -- path")
                keepGoing = False
                break

        if len(domain) < 1:
            print("ERROR -- domain")
            keepGoing = False
            break

        if not a(domain[0]):
            print("ERROR -- domain")
            keepGoing = False
            break

        if i != len(strList):
            if not letDig(domain[1:]):
                print("ERROR -- domain")
                keepGoing = False
                break
        else:
            if not letDig(domain[0:len(domain) - 2]):
                print("ERROR -- domain")
                keepGoing = False
                break

    if not keepGoing: continue

    lastStr = lastStr.rstrip()
    finalChar = lastStr[-1]



    if finalChar != '>':
        print("ERROR -- path")
        continue

    print("Sender ok")