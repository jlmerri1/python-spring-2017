f = open('rosalind_ini5.txt', 'r')
my_list = f.readlines()
count = 0
for x in my_list:
    x = x.strip()
    if count % 2 == 1:
        print x
    count += 1
f.close()