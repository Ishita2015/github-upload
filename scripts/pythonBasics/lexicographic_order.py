from itertools import combinations


if __name__ == '__main__':
    s = input('Enter string: ')
    n = int(input('Enter number: '))
    s = sorted(s)
    for i in range(1, n+1):
        li = list(combinations(s, i))
        for j in li:
            li = ''.join(j)
            print(li)
