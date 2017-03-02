f = open('rosalind_rna.txt', 'r')
input = f.readline()
input = input.rstrip('\n')


def transcribe(text):
    trans_text = ''

    for i in text:
        if i == 'T':
            trans_text += 'U'
        else:
            trans_text += i

    return trans_text


#print transcribe(input)


