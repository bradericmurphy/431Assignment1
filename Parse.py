import sys, re, io
inPt = sys.stdin


pattern = r"(^[\w.+-]+@[\w-]+\.[\w-.]+$)"

for pattern in inPt:
    print (pattern.rstrip("\r\n"))
