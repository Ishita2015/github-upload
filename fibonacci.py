def fibonacci(n):
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    n1 = int(input('Enter first term: '))
    n2 = int(input('Enter second term: '))
    terms = int(input('Enter number of terms: '))
    print('Nth Term: ', fibonacci(terms), sep='')
    print("Fibonacci sequence: ", end='')
    for i in range(1, terms+1):
        print(fibonacci(i), end=' ', sep='')

