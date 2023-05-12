# k Smallest element
# Some possible exam questions is to sort form high to low, make a tertiary sort

from random import randint


def k_smallest_element(elements, k):
    pivot = elements[k]
    low = [x for x in elements if x < pivot]
    if k < len(low):
        return k_smallest_element(low, k)

    k -= len(low)
    equal = [x for x in elements if x == pivot]
    if k < len(equal):
        return pivot

    k -= len(equal)
    high = [x for x in elements if x > pivot]
    return k_smallest_element(high, k)


def median(elements):
    k = (len(elements) - 1) // 2
    return k_smallest_element(elements, k)


def test():
    print("Testing...")
    for _ in range(10000):
        n = randint(1, 100)
        a = [randint(0, 99) for _ in range(n)]
        copy = a[:]
        copy.sort()
        expected_median = copy[(len(copy) - 1) // 2]
        assert median(a) == expected_median
    print("Done")


def main():
    a = [randint(0, 99) for _ in range(20)]

    copy = a[:]
    copy.sort()
    print(copy)

    print(median(a))
    print(k_smallest_element(a, 2))


if __name__ == "__main__":
    test()
    main()
