def check_palindrome(text):
    temp_list = text.split()
    temp_str = ''.join(temp_list)
    main_temp = ''
    for i in range(len(temp_str)):
        main_temp += temp_str[-i-1]
    if main_temp.lower() == temp_str.lower():
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


if __name__ == '__main__':
    text = input("Enter string: ")
    check_palindrome(text)


