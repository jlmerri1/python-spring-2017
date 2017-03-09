f = open('rosalind_ba4j.txt', 'r')
amino_acid_string = f.readline()
amino_acid_string = amino_acid_string.rstrip('\n')


def amino_acid_mass(amino_acid):
    mass = {'G': 57, 'A': 71, 'S': 87,
                   'P': 97, 'V': 99, 'T': 101,
                   'C': 103, 'I': 113, 'L': 113,
                   'N': 114, 'D': 115, 'K': 128,
                   'Q': 128, 'E': 129, 'M': 131,
                   'H': 137, 'F': 147, 'R': 156,
                   'Y': 163, 'W': 186}
    return mass[amino_acid]


def find_mass(amino_acid):
    mass = 0
    for i in amino_acid:
        mass += amino_acid_mass(i)
    return mass


def linear_spectrum(peptide):
    prefix_mass = list()
    prefix_mass.append(0)

    length = 1
    while length <= len(peptide):
        for i in xrange(len(peptide) - length + 1):
            j = peptide[i:length + i]
            prefix_mass.append(find_mass(j))
        length += 1
    return prefix_mass

#lin_spec = linear_spectrum(amino_acid_string)
#lin_spec = sorted(lin_spec)

#for i in lin_spec:
    #print i,




