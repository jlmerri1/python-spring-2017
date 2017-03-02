f = open('rosalind_ba1c.txt', 'r')
dna = f.readline()
dna = dna.strip()
newDna = ''
convert = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
for x in dna:
    newDna  = newDna + '' + convert[x]
print newDna[::-1]
f.close()