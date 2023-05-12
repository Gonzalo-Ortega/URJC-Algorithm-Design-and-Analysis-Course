# Hilo rojo

def binary_search(data, number, low, high):
    if low > high:
        return None
    middle = (low + high) // 2
    if data[middle] == number:
        return middle
    elif number < data[middle]:
        return binary_search(data, number, low, middle - 1)
    else:
        return binary_search(data, number, middle + 1, high)


def main():
    size_1 = int(input().strip())
    data_1 = list(map(int, input().strip().split()))
    size_2 = int(input())
    data_2 = list(map(int, input().strip().split()))

    iterations = int(input().strip())
    for _ in range(iterations):
        number_1, number_2 = map(int, input().strip().split())
        search_1 = binary_search(data_1, number_1, 0, size_1 - 1)
        search_2 = binary_search(data_2, number_2, 0, size_2 - 1)

        if search_1 is not None and search_2 is not None:
            print(str(search_1) + " " + str(search_2))
        else:
            print("SIN DESTINO")


if __name__ == "__main__":
    main()
