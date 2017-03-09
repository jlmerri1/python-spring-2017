from linear_sequence import find_mass


f = open('rosalind_ba4c.txt', 'r')
amino_acid_string = f.readline()
amino_acid_string = amino_acid_string.rstrip('\n')


def cyclspectrum(peptide):
    prefix_mass = list()
    prefix_mass.append(0)
    length = 1
    index = 0
    pep_length = len(peptide)
    prefix_mass.append(find_mass(peptide))
    while length < pep_length:
        for i in xrange(len(peptide) - length + 1):
            j = peptide[i:length + i]
            prefix_mass.append(find_mass(j))
        length += 1
        peptide += peptide[index]
        index += 1
    return prefix_mass

cyspec = cyclspectrum(amino_acid_string)
cyspec = sorted(cyspec)

for i in cyspec:
    print i,
