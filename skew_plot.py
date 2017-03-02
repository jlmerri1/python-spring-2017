import matplotlib.pyplot as plt


f = open('data1.txt', 'r')
file = f.readline()
file = file.rstrip('\n')


def skew(text):
    my_list = []
    count_c = 0
    count_g = 0
    my_list.append(0)
    result_list = []

    for i in xrange(len(text)):
        if text[i] == 'C':
            count_c += 1
        elif text[i] == 'G':
            count_g += 1
        my_list.append(count_g - count_c)

    min_count = min(my_list)

    for idx, val in enumerate(my_list):
        if my_list[idx] == min_count:
            result_list.append(idx)

    return my_list


result = skew(file)
for idx, val in enumerate(result):
    print val

f.close()

plt.plot(result)
plt.title('Skew Diagram')
plt.xlabel('Position')
plt.ylabel('Skew')
plt.show()