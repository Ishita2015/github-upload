def check_sum(dob):
    sum = 0
    age = str(dob)
    for i in age:
        sum += int(i)
    if sum > 9:
        return check_sum(sum)
    else:
        return sum


if __name__ == '__main__':
    dob = int(input("Enter you date of birth: "))
    digit_of_life = check_sum(dob)
    print("Digit of Life is: ", digit_of_life)
