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

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])

s1 = '12.8'
i = float(s1)
print(i)
s2 = str(i)
f = float(s2)
print(s1 == s2)


