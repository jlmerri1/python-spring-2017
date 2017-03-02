f = open('rosalind_ba4a.txt','r')
rna = f.readline()
rna = rna.rstrip('\n')


def translation(text):
    peptide = ''
    aminoADict = {'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                  'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                  'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                  'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                  'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                  'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                  'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                  'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                  'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                  'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                  'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
                  'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                  'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STP', 'UAG': 'STP',
                  'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                  'UGU': 'C', 'UGC': 'C', 'UGA': 'STP', 'UGG': 'W',
                  'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                  }
    length = len(text) - 2
    for i in range(0,len(text)-2, 3):
        codon = text[i:i+3]
        peptide += aminoADict[codon]
    return peptide


#print translation(rna)