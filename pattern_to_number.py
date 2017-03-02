f = open('rosalind_ba1l.txt', 'r')
text = f.readline()
text = text.strip()


def pattern_to_number(pattern):
    d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if pattern is '':
        return 0
    letter = pattern[len(pattern)-1:len(pattern)]
    prefix = pattern[0:len(pattern)-1]
    value = d[letter]
    return 4 * pattern_to_number(prefix) + value

#print pattern_to_number(text)

f.close()
