import math


def calculate(a):
    if 2 * 10**9 >= a >= 1:
        num = math.log2(a)
        num = math.ceil(num)
        return (num)
    else:
        raise Exception("Invalid input.")


input_str = input()
a = int(input_str)
res = calculate(a)
print(res)
