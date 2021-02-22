if __name__ == '__main__':
    n = int(input("Enter number rows: "))
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end="")
        print()

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
