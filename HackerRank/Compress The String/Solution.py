# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import itertools

for line in sys.stdin:
    encodings = []
    for group, items in itertools.groupby(line):
        length = len(list(items))
        compression = (length, group)
        encodings.append(compression)
    
    for tup in encodings:
        tup_formatted = "({0})".format(', '.join(map(str, tup)))
        print(tup_formatted, end=' ')
