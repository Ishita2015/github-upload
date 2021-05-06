# # print(2+3*5)
# # print(1/1)
# # print(1//2*3)
# # print(1/2+3//3+4**2)
# # print(2%2.0)
# # var = 0  # Assigning 0 to var
# # print(var == 0)
# #
# # var = 1  # Assigning 1 to var
# # print(var == 0)
# #
# # x = 1
# # y = 1
# # z = "1"
# #
# # if x == y:
# #     print("one")
# # if y == int(z):
# #     print("two")
# # elif x == y:
# #     print("three")
# # else:
# #     print("four")
# #
# # i = 1
# # j = not not i
# # print(j)
# #
# # for i in range(-1, -2):
# #     print("#")
# #
tup = [1,2,4,8]
#tup = tup[1:-1]
# tup = tup[3:-2]
# print(tup)
print('sMITH' > 'Smithhs')
print('21' < '18')
# tup = tup[0]
# print(tup)
# #
# # mylist = [[0, 1, 2, 3] for i in range(2)]
# # print(mylist[0][1])
# #
# # dict = {'a': 'apple', 'b': 'ball', 'd': 'dog', 'c': 'cat'}
# # # dictionaries are ordered from 3.6 python version onwards
# # print(dict)
# #
# # x=1
# # y=2
# # x,y,z = x,x,y
# # z,y,z = x,y,z
# # print(x,y,z)
# #
from platform import platform, machine, processor, system, version

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())
# #
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

# # for ch in "abc123XYX":
# #     if ch.isupper():
# #         print(ch.lower(), end='')
# #     elif ch.islower():
# #         print(ch.upper(), end='')
# #     else:
# #         print(ch, end='')
#
#
# def name(n):
#     print('ishita ' + n, end='')
#     return ''
#
# if __name__ == '__main__':
#     n = input('Enter something:')
#     for i in range(3):
#         #print('xyz', end=' ')
#         print(name(n), end='')
#
#

# print(float("1, 3"))
#
# print('Mike' > "Mikey")


list = "don't think, do it!".split(' ')
print(list)
x = "\\\\"
print(len(x))

try:
    print('5'/0)
except ArithmeticError:
    print('arith')
except:
    print('some')

print(float("1.3"))

