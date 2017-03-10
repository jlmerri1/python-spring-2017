from transcribe import transcribe
from translation import translation
from reverse_compliment import rev_comp

f = open('rosalind_orf.txt', 'r')
text = f.readlines()
dna_string = ''
for i in text:
    i = i.rstrip('\n')
    i = i.rstrip('\t')
    dna_string += i


def open_reading_frames(rna):
    start = 0
    peptide = translation(rna)
    proteins = []

    while not start == -1:
        start = peptide.find('M', start)
        stop = peptide.find('STP', start + 1)
        if not stop == -1:
            pep = peptide[start:stop]
            if pep:
                proteins.append(pep)
        if not start == -1:
            start += 1
    return proteins


def all_frames(dna):
    rna = transcribe(dna)
    comp_rna = transcribe(rev_comp(dna))
    proteins = []
    for i in xrange(0,3):
        proteins += open_reading_frames(rna[i:])
        proteins += open_reading_frames(comp_rna[i:])
    return list(set(proteins))


output = open_reading_frames('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')

for i in output:
    print i
