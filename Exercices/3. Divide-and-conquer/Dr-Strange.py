# Dr. Strange

def binary_search(data, string, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    if data[middle] == string:
        return middle
    elif string < data[middle]:
        return binary_search(data, string, low, middle - 1)
    else:
        return binary_search(data, string, middle + 1, high)


def main():
    data = input().split()
    data.sort()
    iterations = int(input().strip())
    for _ in range(iterations):
        string = input()
        index = binary_search(data, string, 0, len(data) - 1)
        if index == 0 or index is None:
            print("VACIO", end=" ")
        else:
            print(str(data[index - 1]), end=" ")
        if index == len(data) - 1 or index is None:
            print("VACIO")
        else:
            print(data[index + 1])


if __name__ == "__main__":
    main()
