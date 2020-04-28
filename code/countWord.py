fhand = open('rnj.txt')
myDict = dict()
for line in fhand:
    line = line.rstrip()
    if len(line) == 0 :
        continue
    for itr in line.split():
        myDict[itr] = myDict.get(itr,0)+1
for keys in myDict:
    print(keys, myDict[keys] )
print(myDict)
fhand.close()
