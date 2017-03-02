from eight_copy import function
f = open('rosalind_ba1b.txt', 'r')
sample = f.readlines()
a = sample[0]
a = a.strip()
b = sample[1]
b = b.strip()
b = int(b)
count = 0
d = {}
for x in xrange(len(a) - b):
    the_pattern = a[x:b + x]
    if the_pattern not in d.values():
        (count) = function(a, the_pattern)
        d[the_pattern] = count
m = max(d.values())
for key, value in d.items():
    if m == value:
        print key,
f.close()
