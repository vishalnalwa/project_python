dict = { 'one' : 'ek' , 'two' : 'do' , 'three' : 'teen'}
l = list()

for key , val in list(dict.items()):
    l.append((val, key))
l.sort()
print(l)
