def check_anagrams(str1, str2):
    if str1 == '' or str2 == '':
        print("not anagrams")
    elif len(str1) != len(str2):
        print("Not anagrams")
    else:
        count = 0
        for i in str1:
            if str1.count(i) != str2.count(i):
                print("Not anagrams")
                count = 1
                break
            else:
                continue
        if count == 0:
            print("Anagrams")


if __name__ == '__main__':
    string1 = input("Enter your first string").lower()
    string2 = input("Enter your second string").lower()
    check_anagrams(string1, string2)
