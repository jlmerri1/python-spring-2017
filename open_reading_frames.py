from transcribe import transcribe
from translation import translation
from codon_dict import codonDict

f = open('rosalind_orf.txt', 'r')
dna = f.readlines()
dna_string = ''
for i in dna:
    i = i.rstrip('\n')
    i = i.rstrip('\t')
    dna_string += i


def open_reading_frames(text):
    protein_cand = list()
    protein = ''
    rna1RFrame1 = ''
    rna1RFrame2 = ''
    rna1RFrame3 = ''
    rna2RFrame1 = ''
    rna2RFrame2 = ''
    rna2RFrame3 = ''
    rna1 = ''
    rna1 = transcribe(text)
    rna2 = ''
    rna2 = transcribe(text[::-1])

    rna1RFrame1 = rna1[:]
    rna1RFrame2 = rna1[1:]
    rna1RFrame3 = rna1[2:]
    rna2RFrame1 = rna2[:]
    rna2RFrame2 = rna2[1:]
    rna2RFrame3 = rna2[2:]

    rna1RFrame1 = translation(rna1RFrame1)
    rna1RFrame2 = translation(rna1RFrame2)
    rna1RFrame3 = translation(rna1RFrame3)
    rna2RFrame1 = translation(rna2RFrame1)
    rna2RFrame2 = translation(rna2RFrame2)
    rna2RFrame3 = translation(rna2RFrame3)

    numM = rna1RFrame1.find('M')
    numSTP = rna1RFrame1.find('STP')




    return rna1RFrame1, numM, numSTP



print open_reading_frames('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')