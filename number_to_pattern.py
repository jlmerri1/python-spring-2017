f = open('rosalind_ba1m.txt', 'r')
text = f.readlines()
index = text[0]
index = index.strip()
index = int(index)
k = text[1]
k = k.strip()
k = int(k)


def number_to_pattern(i, k_num):
    d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k_num is 1:
        return d[i]
    prefix_index = i / 4
    r = i % 4
    letter = d[r]
    prefix_pattern = number_to_pattern(prefix_index, k_num - 1)
    prefix_pattern += letter
    return prefix_pattern


#print number_to_pattern(index, k)
f.close()
