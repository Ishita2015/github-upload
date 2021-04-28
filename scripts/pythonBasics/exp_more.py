# class A:
#     A = 1
#     def __init__(self, v=2):
#         self.v = v + A.A
#         A.A += 1
#
#     def set (self, v):
#         self.v += v
#         A.A += 1
#         return
# a = A()
# a.set(2)
# print(a.v)
#
# x = """
# """
# x = '\\'
# print(len(x))
#
# # lt = [1,2,3,4]
# # lt = list(map(lambda x: 2*x, 1))
# # print(lt)
#
# d = {'one': 1, 'three': 3, 'two': 2}
# for k in sorted(d.values()):
#     print(k)
#
# print(len([i for i in range(0, -2)]))
# print(len((1, )))
#
# z=2
# y=1
# x = z<y
# print(x)
#
# ls = [[c for c in range(r)] for r in range(3)]
# for x in ls:
#     if len(x) < 2:
#         print(len(x))
#         print('a')

# i = 4
# while i <= 4:
#     i -= 2
#     print('*')
#     if i == 2:
#         break
# else:         # execute when while condition is false
#     print("ishi")
#
# class A:
#     def __init__(self, v):
#         self.__a = v + 1
#
# a = A(0)
# print(a.__a)
#
# list = [1,2,3,4]
# print(list[-3:-2])
#
# x= 1
# y = 2
# x,y,z = x,x,y
# z,y,z = x,y,z
# print(x,y,z)
#
# lst = [i for i in range(1, -1)]
# print(lst)
# #
# tup = (1,2,4,8)
# tup = tup[-2:-1]
# print(tup)
# tup = tup[-1]
# print(tup)
#
#
# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)
#
# b = bytearray(3)
# print(b)

# s = "abcdef"
# print(s[::2])
#
# import os
# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumb')
# os.chdir('thumb')
# os.mkdir('temp')
# os.chdir('../')
#
# print(os.getcwd())

# from datetime import datetime
# datetime = datetime(2019, 11, 27,11,27,22)
# print(datetime.strftime('%Y/%m/%d %H:%M:%S'))
# print(datetime.strftime('%y/%B/%d %H:%M:%S'))
# import calendar
# print(calendar.weekheader(9))

# datetime_1 = datetime(2019, 11, 27,11,27,22)
# datetime_2 = datetime(2019, 11, 27,0,0,0)
# print(datetime_1- datetime_2)

# print(__name__)
#
# class A:
#     def __init__(self):
#         pass
# a = A()
# print(hasattr(a, 'A'))
#
# class X:
#     pass
# class Y(X):
#     pass
# class Z(Y):
#     pass
# x = Z()
# z = Z()
#
# print(isinstance(x, Z), isinstance(x, Y), isinstance(x, X), isinstance(z, Z), isinstance(z, X), isinstance(Z, X))

# import platform, os
# print(platform.uname())
# print(os.name)
#
# os.mkdir("my_directory")
# print(len(os.listdir()))
#
