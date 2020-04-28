def chop(l):
    del l[0]
    last_index = len(l)-1
    del l[last_index]

def chopNew(l):
    last_index = len(l)-1
    l = l[1:last_index]

myList = [1,2,3,4,5]
print(id(myList))
chopNew (myList)
print(myList)
print(id(myList))
