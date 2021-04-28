msj = input("Enter msj: ")
shift_value = int(input("Enter shift value: "))
while shift_value < 1 or shift_value > 25:
    shift_value = int(input("Enter valid shift value: "))
cipher = ''
for char in msj:
    if char.isalpha():
        code = ord(char) + shift_value
        if char.isupper():
            if code > ord('Z'):
                code = code - ord('Z') + ord('A') - 1
        if char.islower():
            if code > ord('z'):
                code = code - ord('z') + ord('a') - 1
        cipher += chr(code)
    else:
        cipher += char
print(cipher)

