# Tentadores
# Binary search increasing the list and saving the index of sorted and then inserted elements.

def binary_search(items, item, low, high):
    if low > high:
        return low
    middle = (low + high) // 2
    if items[middle] == item:
        return middle
    elif item < items[middle]:
        return binary_search(items, item, low, middle - 1)
    else:
        return binary_search(items, item, middle + 1, high)


def main():
    items_amount, new_items_amount = map(int, input().strip().split())

    items = list(input().strip().split())
    items.sort()

    for _ in range(new_items_amount):
        item = input().strip()
        index = binary_search(items, item, 0, len(items) - 1)
        print(item + ": " + str(index))
        items.insert(index, item)

    print(*items)


if __name__ == "__main__":
    main()
