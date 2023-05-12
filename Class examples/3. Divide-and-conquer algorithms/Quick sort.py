def partition2(v, left, right):
    pivot = v[left]
    i, j = left + 1, right

    while True:
        while i <= j and v[i] <= pivot:
            i += 1
        while i <= j and v[j] > pivot:
            j -= 1
        if i > j:
            break
        v[i], v[j] = v[j], v[i]

    v[left], v[j] = v[j], v[left]
    return j


def partition(v, left, right):
    pivot = v[left]

    i = left + 1
    while i < right and v[i] <= pivot:
        i += 1
    j = right
    while j > left and v[j] > pivot:
        j -= 1

    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        while v[i] <= pivot:
            i += 1
        j -= 1
        while v[j] > pivot:
            j -= 1

    v[left], v[j] = v[j], v[left]
    return j


def quick_sort_recursive(array, i, j):
    if j < i:
        return array
    else:
        idx = partition(array, i, j)
        quick_sort_recursive(array, i, idx - 1)
        quick_sort_recursive(array, idx + 1, j)


def quickSort(elements):
    quick_sort_recursive(elements, 0, len(elements) - 1)
