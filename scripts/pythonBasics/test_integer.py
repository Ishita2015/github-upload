if __name__ == '__main__':
    n = int(input('Enter any integer: '))
    if n%2 == 0 and n<5:
        print('1')
        print("Not Weird")
    elif n%2 == 0 and 5<n<21:
        print('2')
        print("Weird")
    elif n%2 == 0 and n>20:
        print('3')
        print("Not Weird")
    elif n%2 != 0:
        print('4')
        print("Weird")
