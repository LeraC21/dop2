from functools import reduce


def reduce_fun(prev, tec):
    if tec[0] > prev[0]:
        print(tec[0], ' '.join(tec[1]))
        return tec
    else:
        return prev


f = open('news.txt', 'r', encoding="utf8")
array = []
for line in f.readlines():
    count, *post = line.split()
    array.append([int(count), post])

print(array[0][0], ' '.join(array[0][1]))
reduce(reduce_fun, array)