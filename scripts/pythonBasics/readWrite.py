file = open('test.txt')
# read all the contents of file
print(file.read(1))
# read single line at a time
# print(file.readline())
# print(file.readline())

# print line by line using readline method
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# using readlines method

# var = file.readlines()
# print(var[4])
for line in file.readlines():
    print(line)

file.close()
