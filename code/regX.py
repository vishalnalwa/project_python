#learn regular expression
import re
valid = '^X-\S* ([bo    +)'
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall(valid, line)
    if len(x) > 0:
        print(x)
