def is_leap(year):
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap


if __name__ == '__main__':
    year = int(input('Enter any year: '))
    print(is_leap(year))
