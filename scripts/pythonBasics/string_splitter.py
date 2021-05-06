# string = 'aa_b%%%%b_c_a'
# tempstr1 = string.split('%')
# tempstr2 = '_'.join(tempstr1)
# final_str = tempstr2.split('_')
# final_str = [i for i in final_str if i]
# print(final_str)


def string_splitter(string, set_sep):
    temp_list = []
    temp_str = ''
    for ch in range(len(string)):
        if string[ch] not in set_sep:
            temp_str += string[ch]
            if ch == len(string) - 1:
                temp_list.append(temp_str)
        else:
            temp_list.append(temp_str)
            temp_str = ''
    temp_list = [i for i in temp_list if i]
    return temp_list


if __name__ == '__main__':
    string = 'aa_b%%%%b_c_a'
    set_sep = ('%', '_')
    final_list = string_splitter(string, set_sep)
    print(final_list)

