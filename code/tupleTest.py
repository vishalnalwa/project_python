txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
#t.sort()
words.sort(key=len)
#res = list()
#for length, word in t:
#    res.append(word)
print(words)
#print(res)
