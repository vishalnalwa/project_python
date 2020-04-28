fhand = open('words.txt')
myDict= dict()
spChars='[@_!#$%^&*()<>?/\|}{~:-]'
for line in fhand:
    line=line.rstrip()
    if len(line)==0:
        continue
    for itr in line.split():
        for c in itr:
            if c in spChars:
                continue
            print(c)
            myDict[c.upper()]=myDict.get(c.upper(),0)+1
#            if c.upper() not in myDict:
#                myDict[c.upper()]=1
#            else:
#                myDict[c.upper()]=myDict[c.upper()]+1
print(myDict)
fhand.close()

#        print(itr)
#        myDict[itr]=''
#print(myDict)
#fhand.close()
