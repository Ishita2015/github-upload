def check_palindrome(string):
    temp_str = string
    list = []
    n = len(temp_str)+1
    for i in range(-1, -n, -1):
        list.append(temp_str[i])
    temp_str_final = ''.join(list)
    if temp_str_final == string:
        return True
    else:
        return False


if __name__ == '__main__':
    string = input('Enter string: ')
    print('Given string is Palindrome:', check_palindrome(string))
