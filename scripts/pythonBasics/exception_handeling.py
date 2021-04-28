def read_int(prompt, min, max):
    global result
    while True:
        try:
            result = int(input(prompt))
            break
        except ValueError:
            print('Error: wrong input')
            continue
    while result < min or result > max:
        print("Error: the value is not within permitted range (min..max)")
        while True:
            try:
                result = int(input(prompt))
                break
            except ValueError:
                print('Error: wrong input')
                continue
    return result


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

