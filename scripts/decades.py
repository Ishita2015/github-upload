# program to calculate the the decades based on person's age.


def cal_decades(age):
    decades = age / 10
    years = age % 10
    print('You are ' + str(decades) + ' decades and ' + str(years) + ' years old.')


def main():
    attempts = int(input('Enter number of attempts:'))
    for i in range(attempts):
        age = int(input('Enter your age:'))
        cal_decades(age)


main()
