def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    main = int((columns - 7)/2)
    rowlimit = int(rows/2)
    middlepattern = ".|."
    dash = "-"
    # print upper half of the pattern
    j = 0
    for i in range(1, rowlimit+1):
        dashcount = (int((columns - len(middlepattern)*(j+1))/2))
        print(dashcount * dash, middlepattern * (j+1), dashcount * dash, sep='')
        j = j+2
    # print middle of the pattern
    print(main * '-', 'WELCOME', main * '-', sep='')
    # print lower half of the pattern
    for i in range(rowlimit+2, rows+1):
        dashcount = (int((columns - len(middlepattern)*(j-1))/2))
        print(dashcount * dash, middlepattern * (j-1), dashcount * dash, sep='')
        j = j-2

    # first = int((columns - 3)/2)
    # second = int((columns - 9)/2)
    # third = int((columns - 15)/2)
    # print(first*'-', s, first*'-', sep='')
    # print(second*'-', 3*s, second*'-', sep='')
    # print(third*'-', 5*s, third*'-', sep='')
    # print(third*'-', 5*s, third*'-', sep='')
    # print(second*'-', 3*s, second*'-', sep='')
    # print(first*'-', s, first*'-', sep='')


if __name__ == "__main__":
    main()
