import re
regEx = input("Enter a regular expression ")
matchCount=0
try:
    fhand = open('mbox.txt')
except:
    print("Error openning the file")
    exit()
for line in fhand:
    line = line.rstrip()
    if re.search(regEx,line):
        matchCount+=1
print( 'mbox.txt had', matchCount,'lines that matched', regEx)
