# this program prints the largest number in the given list
def largest(list):
    largest = None
    print (" Before : ", largest)
    for itr in list:
        if largest == None or itr > largest:
            largest = itr
    return largest


largest = largest([3, 41, 12, 9, 74, 15])
print("largest number in the list is", largest)
