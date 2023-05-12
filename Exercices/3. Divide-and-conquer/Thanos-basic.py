def main():
    size = input()  # Not used
    data = input()  # Not used
    size = int(input().strip())
    data = set(map(int, input().strip().split()))
    iterations = input()  # Not used
    iterations = list(map(int, input().strip().split()))
    for number in iterations:
        if number in data:
            print(":_(")
        else:
            print(":)")


if __name__ == "__main__":
    main()
