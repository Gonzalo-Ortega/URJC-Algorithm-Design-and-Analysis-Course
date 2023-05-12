# Merge sort

from random import randint


def merge(first, second, output):
    f = s = k = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1

    r = f if s == len(second) else s
    reminder = first if s == len(second) else second

    for i in range(r, len(reminder)):
        output[k] = reminder[i]
        k += 1


def merge_sort(elements):
    if len(elements) == 1: #ojo que podría merecer la pena ordenar con un método iterativo
        return
    else:
        middle = len(elements) // 2
        left = elements[:middle]
        right = elements[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, elements)


def test():
    print("Testing...", end=" ")
    for _ in range(100000):
        vector = []
        n = randint(1, 100)
        for j in range(n):
            vector.append(randint(-50, 50))
        copy = vector[:]
        mergeSort(vector)
        copy.sort()
        assert copy == vector
    print("Done")

testMergeSort()
