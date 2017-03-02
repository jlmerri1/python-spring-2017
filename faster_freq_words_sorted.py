from pattern_to_number import pattern_to_number
from number_to_pattern import number_to_pattern


f = open('data.txt', 'r')
input = f.readlines()
text = input[0]
text = text.strip()
k = input[1]
k = k.strip()
print text, k
k = int(k)

def faster_freq_words_sorted(text, k):
    freq_words = []
    counts = [1] * (len(text) - k)
    indices = []

    for i in xrange(len(text) - k):
        pattern = text[i: i + k]
        indices.append(pattern_to_number(pattern))

    indices.sort()
    for i in xrange(1, len(indices)):
        if indices[i] == indices[i - 1]:
            counts[i] = counts[i - 1] + 1

    max_counts = max(counts)
    for i in xrange(0, len(counts)):
        if counts[i] == max_counts:
            pattern = number_to_pattern(indices[i], k)
            freq_words.append(pattern)
    return freq_words


print faster_freq_words_sorted(text, k)

