import re
try:
    fhand = open('mbox-short.txt')
except:
    print('Error while opening the file')
    exit()
count = 0
hour_of_the_day = 0
myDict = dict()
myList = list()
for line in fhand:
    line = line.rstrip()
    x= re.findall('^From .* ([0-9][0-9]):',line)
    if len(x)>0:
        print(x)
