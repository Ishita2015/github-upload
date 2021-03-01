ItemsCart = 0
# 2 items will be added to cart

if ItemsCart != 2: #raise Exception("Products cart count is not matching")
    pass

assert (ItemsCart == 0)
#assert (ItemsCart == 2)

# try except in python

try:
    with open('test.txt', 'r') as reader:
        print(reader.read())

except:
    print('Failure in try block')

try:
    with open('randomfile.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('finally block is reached')



