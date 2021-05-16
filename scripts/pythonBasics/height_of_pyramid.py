blocks = int(input("Enter the number of blocks: "))
sum = 0
for i in range(1,blocks+1):
    sum = sum + i
    if sum > blocks:
        break

height = i-1
print("The height of the pyramid:", height)
