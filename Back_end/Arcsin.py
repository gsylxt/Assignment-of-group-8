import math


def arcsin(x):
    precision = 0.0000001
    if not -1 <= x <= 1:
        return 'err'
    result = 0
    # （-0.9,0.9）时，arcsin的泰勒尔展开式收敛速度较快，采用arcsin的泰勒尔展开式计算
    if -0.9 <= x <= 0.9:
        result = x
        term = x
        i = 0
        while abs(term) > precision:
            term *= (x * x * (2 * i + 1) * (2 * i + 1)) / ((2 * i + 2) * (2 * i + 3))
            result += term
            i += 1
    # x>0.9时，收敛速度较慢，采用arcsin(x)=arctan(x/（1-x^2)^0.5)进行转换计算
    elif x > 0.9:
        x = (1 - x ** 2) ** 0.5 / x
        term = x - x ** 3 / 3
        n = 1
        while abs(term) > precision:
            result += term
            term = x ** (2 * n + 3) / (2 * n + 3) - x ** (2 * n + 5) / (2 * n + 5)
            n += 2
        result = 0.5 * math.pi - result
    else:
        x = - (1 - x ** 2) ** 0.5 / x
        term = x - x ** 3 / 3
        n = 1
        while abs(term) > precision:
            result += term
            term = x ** (2 * n + 3) / (2 * n + 3) - x ** (2 * n + 5) / (2 * n + 5)
            n += 2
        result = - (0.5 * math.pi - result)
    result = 180*result/math.pi
    return result
