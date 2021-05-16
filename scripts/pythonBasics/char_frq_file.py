# file_path ------ 'C:\Users\ishita_nigam\scripts\pythonBasics\test.txt'


def char_frq(file):
    file = open(file, mode='r')
    lines = file.readlines()
    lines = ''.join(lines).lower()
    char_dict = {}
    for ch in lines:
        cnt = lines.count(ch)
        char_dict[ch] = cnt
    for char, frq in char_dict.items():
        if char != '\n':
            print(char, "-->", frq)


if __name__ == '__main__':
    input_file = input("Enter file's path: ")
    char_frq(input_file)
