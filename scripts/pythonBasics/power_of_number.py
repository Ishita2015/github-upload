def check_number(n, p):
    while n > 1:
        if n % p == 0:
            n = n/p
        else:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Enter number: '))
    p = int(input('Enter power: '))
    print('Number', n, 'is the power of', p, ': ', check_number(n, p))
