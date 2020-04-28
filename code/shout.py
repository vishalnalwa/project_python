try:
    fhand = open('mbox.txt')
except:
    print("Failed to open the file")
    exit()
myDict=dict()
myList=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        day = (line.split())[1]
        myDict[day] = myDict.get(day,0)+1
for email , count in myDict.items():
    myList.append((count,email))
myList.sort(reverse=True)

for count , email in myList:
    print (email , " " , count)
