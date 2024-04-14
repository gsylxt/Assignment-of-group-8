import math


def arctan(x):
    precision = 0.000001
    result = 0
    if -1 <= x <= 1:
        term = x - x ** 3 / 3
        n = 1
        while abs(term) > precision:
            result += term
            term = x ** (2 * n + 3) / (2 * n + 3) - x ** (2 * n + 5) / (2 * n + 5)
            n += 2

    elif x > 1:
        x = 1 / x
        term = x - x ** 3 / 3
        n = 1
        while abs(term) > precision:
            result += term
            term = x ** (2 * n + 3) / (2 * n + 3) - x ** (2 * n + 5) / (2 * n + 5)
            n += 2
        result = 0.5 * math.pi - result
    else:
        x = - 1 / x
        term = x - x ** 3 / 3
        n = 1
        while abs(term) > precision:
            result += term
            term = x ** (2 * n + 3) / (2 * n + 3) - x ** (2 * n + 5) / (2 * n + 5)
            n += 2
        result = - (0.5 * math.pi - result)
    # 将计算结果的弧度改为角度
    result = 180*result/math.pi
    return result