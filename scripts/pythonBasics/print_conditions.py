if __name__ == '__main__':
    # to print without spaces
    print("Hello", "Ishita", sep='')
    # to print with spaces
    print("Hello", "Ishita")
    # to print in newline
    print("Hello", "Ishita", sep='\n')
    # if we call print function in a for loop then it is separated by newline by default
    for i in range(1, 4):
        print(i)
    # if we call print function in a for loop then want to print without spaces
    for i in range(1, 4):
        print(i, end='')
