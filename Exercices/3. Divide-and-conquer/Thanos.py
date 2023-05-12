# Thanos
# DOES NOT WORK

def bool_binary_search(data, number, low, high):
    if low > high:
        return False
    middle = (low + high) // 2
    if data[middle] == number:
        return True
    elif number < data[middle]:
        return bool_binary_search(data, number, low, middle - 1)
    else:
        return bool_binary_search(data, number, middle + 1, high)


def main():
    size = input()  # Not used
    data = input()  # Not used
    size = int(input().strip())
    data = list(map(int, input().strip().split()))
    iterations = input()  # Not used
    iterations = list(map(int, input().strip().split()))
    for number in iterations:
        if bool_binary_search(data, number, 0, size - 1):
            print(":_(")
        else:
            print(":)")


if __name__ == "__main__":
    main()
