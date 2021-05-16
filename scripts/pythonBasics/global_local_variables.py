def fun1():
    f = 'local variable'
    print(f)


def fun2():
    print(f)


def fun3():
    global f
    f = 'global variable'
    print(f)


def fun4():
    print(f)


if __name__ == '__main__':
    f = 11
    print(f)
    fun1()
    fun2()
    fun3()
    fun4()
    print(f)
