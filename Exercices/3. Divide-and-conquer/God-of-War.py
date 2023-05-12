# God of War

def binary_approx_search(data, number, low, high):
    if low > high:
        return high, False
    middle = (low + high) // 2
    if data[middle] == number:
        return middle, True
    elif number < data[middle]:
        return binary_approx_search(data, number, low, middle - 1)
    else:
        return binary_approx_search(data, number, middle + 1, high)


def main():
    size = int(input().strip())
    data = list(map(int, input().strip().split()))
    iterations = int(input().strip())
    iterations = map(int, input().strip().split())
    for number in iterations:
        index, found = binary_approx_search(data, number, 0, size - 1)
        if found:
            if index == 0:
                print("X", end=" ")
            else:
                print(str(data[index - 1]), end=" ")
            if index == len(data) - 1:
                print("X")
            else:
                print(data[index + 1])
        else:
            if index == - 1:
                print("X", end=" ")
            else:
                print(str(data[index]), end=" ")
            if index == size - 1:
                print("X")
            else:
                print(data[index + 1])


if __name__ == "__main__":
    main()
