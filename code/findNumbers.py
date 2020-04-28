import re
regEx = '[0-9]+'
hand = open('mbox-short.txt')
total=0
count=0
for line in hand:
    line = line.rstrip()
    x = re.findall(regEx, line)
    if len(x)>0:
        for itr in x:
            print(itr)
            total = total + int(itr)
            count= count + 1
print(total/count)
