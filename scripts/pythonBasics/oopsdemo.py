class Calculator:
    num = 100 # class variables

    # default constructor
    def __init__(self, a, b):
        self.a = a     # instance variable
        self.b = b
        print('I am automatically called when object is created')

    def getdata(self):
        print('I am executing it')

    def summation(self):
        return self.a + self.b + Calculator.num + self.num
        # return a + b + num + num


obj = Calculator(2, 3)  # syntax to create objects of a class in python
obj.getdata()
print(obj.summation())

obj1 = Calculator(4, 5)  # syntax to create objects of a class in python
obj1.getdata()
print(obj1.summation())

