def check_armstrong(n):
    sum = 0
    temp = n
    order = len(str(n))
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp = int(temp/10)
    if sum == n:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input('Enter number: '))
    print('Number is Armstrong: ', check_armstrong(n))
