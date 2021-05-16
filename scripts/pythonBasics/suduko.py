suduko = []
for i in range(9):
    row = input("Enter rows: ")
    suduko.append(row)
print(suduko)
counter = 0
for row in suduko:
    for j in range(1, 4):
        if str(j) not in row:
            counter = 1
            break
        else:
            continue
    if counter != 0:
        print("No")
        break
    else:
        continue
if counter == 0:
    print("Yes")
