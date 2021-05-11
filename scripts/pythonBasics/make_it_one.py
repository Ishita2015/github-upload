class Solution:

    def check_power(self, n):
        import math
        self.x = math.log(n, 2)
        if self.x == int(self.x):
            return self.x
        else:
            return False

    def re_check_num(self, n):
        from math import pow, log, floor
        self.m = pow(2, floor(log(n, 2)))
        n -= self.m
        return n

    def reduce_num(self, n):
        self.count = 0
        self.m = self.re_check_num(n)
        self.count += 1
        while (self.m > 1):
            self.power = self.check_power(self.m)
            if not self.power:
                self.m = self.re_check_num(self.m)
                self.count += 1
            else:
                self.count = self.count + self.power
                self.m = -1
        return self.count

    def number_of_operations(self, n):
        if not int(n):
            raise ValueError("Only accepts integer values!")
        if n <= 1:
            # print("Number of operation to reduced it One is: 0")
            return 0
        else:
            self.count1 = self.check_power(n)
            if not self.count1:
                self.count2 = self.reduce_num(n)
                return self.count2
            else:
                # print("Number of operation to reduced it One is: ", count1)
                return self.count1
