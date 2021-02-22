def merge_the_tools(s, k):
    # your code goes here
    for i in range(0, len(s), k):
        finalstring = ""
        for j in s[i:i+k]:
            if j not in finalstring:
                finalstring += j
        print(finalstring)


if __name__ == '__main__':
    string, k = input('Enter string: '), int(input('Enter factor k: '))
    merge_the_tools(string, k)
