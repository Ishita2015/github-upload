def find_largest(list):
    temp = 0
    for i in range(0, len(list)):
        if list[i] > temp:
            temp = list[i]
    return temp


def find_second_largest(list):
    temp_list = list
    n = find_largest(temp_list)
    temp_list.remove(n)
    second_largest = find_largest(temp_list)
    return second_largest


if __name__ == '__main__':
    list = [81, 80, 12, 18, 94, 100, 90]
    print("Second largest number is: ", find_second_largest(list))
