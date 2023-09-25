import heapq

with open('./content/median.txt') as f:
    a = [int(x) for x in f]

sort_a = []

median = []

for i in range(1, len(a) + 1):
    sorted_a = heapq.nsmallest(i, a[:i])
    if i/2 * 2 == i:
        median.append(sorted_a[int(i/2) - 1])
        if i % 500 == 0:
            print(i)
    else:
        median.append(sorted_a[(i+1)/2 - 1])

mode = sum(median) % len(a)
print(mode)
