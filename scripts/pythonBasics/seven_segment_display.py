def print_seven_display(mat):
    for i in range(5):
        for j in range(3):
            if mat[i][j] == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def check_digit(num):
    mat_zero = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    mat_one = [[1, 1, 1],
               [1, 1, 1],
               [1, 1, 1],
               [1, 1, 1],
               [1, 1, 1]]
    if num == 0:
        mat_one[1][1], mat_one[2][1], mat_one[3][1] = 0, 0, 0
        print_seven_display(mat_one)
    if num == 1:
        mat_zero[0][0], mat_zero[1][0], mat_zero[2][0], mat_zero[3][0], mat_zero[4][0] = 1, 1, 1, 1, 1
        print_seven_display(mat_zero)
    if num == 2:
        mat_one[1][0], mat_one[1][1], mat_one[3][1], mat_one[3][2] = 0, 0, 0, 0
        print_seven_display(mat_one)
    if num == 3:
        mat_one[1][0], mat_one[1][1], mat_one[3][0], mat_one[3][1] = 0, 0, 0, 0
        print_seven_display(mat_one)
    if num == 4:
        mat_one[0][1], mat_one[1][1], mat_one[3][0], mat_one[3][1], mat_one[4][0], mat_one[4][1] = 0, 0, 0, 0, 0, 0
        print_seven_display(mat_one)
    if num == 5:
        mat_one[1][1], mat_one[1][2], mat_one[3][0], mat_one[3][1] = 0, 0, 0, 0
        print_seven_display(mat_one)
    if num == 6:
        mat_one[1][1], mat_one[1][2], mat_one[3][1] = 0, 0, 0
        print_seven_display(mat_one)
    if num == 7:
        mat_zero[0][0], mat_zero[0][1], mat_zero[0][2], mat_zero[1][2], mat_zero[2][2], mat_zero[3][2], mat_zero[4][2] \
            = 1, 1, 1, 1, 1, 1, 1
        print_seven_display(mat_zero)
    if num == 8:
        mat_one[1][1], mat_one[3][1] = 0, 0
        print_seven_display(mat_one)
    if num == 9:
        mat_one[1][1], mat_one[3][0], mat_one[3][1] = 0, 0, 0
        print_seven_display(mat_one)
    return ''


if __name__ == '__main__':
    number = input('Enter digit: ')
    for n in number:
        print(check_digit(int(n)), end='')



