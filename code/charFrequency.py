import re
import time
start_time= time.time()

valid = '[a-z]'
try:
    fhand = open("mbox.txt")
except:
    print ("Can not open the file!!")
    exit()

charfrequnecy = dict()
alphaline = ''
totalCharsInText=0
myList=list()
frequencyPercentage=0.0
for line in fhand:
    line = line.rstrip()
#    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    for char in line:
#        if re.search(valid,char):
        if char.isalpha():
            charfrequnecy[char]=charfrequnecy.get(char,0)+1
            totalCharsInText+=1
for letter , frequency in charfrequnecy.items():
    frequencyPercentage = (frequency*100)/totalCharsInText
    myList.append((frequencyPercentage,letter))
print(charfrequnecy)
print(totalCharsInText)
myList.sort(reverse=True)
for frequencyPercentage , letter  in myList:
    print(letter, ' ' , '%.3f'%frequencyPercentage)
print("--- %s seconds ---" % (time.time() - start_time))
