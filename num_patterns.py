f = open('rosalind_ba1a.txt', 'r')
sample = f.readlines()
a = sample[0]
a = a.rstrip('\n') #could use strip() or rstrip('\n')
b = sample[1]
b = b.rstrip('\n') #could use strip() or rstrip('\n')
count = 0
for x in xrange(len(a)):
    new_string = a[x:x + len(b)]
    if (new_string == b):
        count = count + 1
print count
f.close()