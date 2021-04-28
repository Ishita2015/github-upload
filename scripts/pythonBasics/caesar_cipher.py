msj = input("Enter message: ")
cipher = ''
for char in msj:
    if not char.isalpha():
        cipher += char
    else:
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

print(cipher)
