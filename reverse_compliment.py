f = open('rosalind_ba1c.txt', 'r')
dna = f.readline()
dna = dna.strip()

def rev_comp(text):
    newDna = ''
    convert = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    for x in text:
        newDna  = newDna + '' + convert[x]
    return newDna[::-1]
#print rev_comp(dna)
f.close()