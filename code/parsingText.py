import string

#filename = input("Enter the file name to parse :")
try:
    fhand = open("words.txt")
except:
    print ("Can not open the file!!")
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    print(line)
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

l = list()
for key , val  in list(counts.items()):
    l.append((val , key))
l.sort(reverse=True)
#list top 10 used words
for key , val in l:
    print ( key , val)
