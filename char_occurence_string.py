def char_count(s):
    for i in range(0, len(s)):
        count = 1
        if i != 0:
            if s[i] == s[i-1]:
                continue
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
            else:
                break
        print('(', count, ', ', s[i], ') ', end='', sep='')


if __name__ == '__main__':
    s = input('Enter string: ')
    char_count(s)
