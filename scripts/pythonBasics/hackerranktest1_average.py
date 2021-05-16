def avrg(nums):
    n = len(nums)
    sum = 0
    for i in nums:
        sum = sum + int(i)
    avg = sum / n
    return(avg)


if __name__ == '__main__':
    nums = input('Enter numbers: ').split(' ')
    res = avrg(nums)
    print('%.2f' % res + '\n')

