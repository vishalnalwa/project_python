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
    if line.startswith("From "):
        hour_of_the_day = int((line.split())[5].split(':')[0])
        myDict[hour_of_the_day] = myDict.get(hour_of_the_day,0)+1
print(myDict)
for hr , count in myDict.items():
    myList.append((hr,count))
    myList.sort()
for hr , count in myList:
    print(hr, ' ' , count)
