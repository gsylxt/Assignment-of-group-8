import math

def cos(number):

    # 将角度转换为弧度
    def to_radians(number):
        return (math.pi / 180) * number

    # 将角度规范为[0, 360]
    def normalize_angle(angle):
        while angle < 0:
            angle += 360
        while angle >= 360:
            angle -= 360
        return angle

    # 定义计算阶乘的函数
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    # 使用泰勒展开计算三角函数
    def cos_taylor(x, error_limit):
        result = 0
        term = 1
        n = 0
        while abs(term) >= error_limit:
            result += term
            n += 2
            term = (-1) ** (n // 2) * (x ** n) / factorial(n)
        return result

    # 设置误差限制
    error_limit = 0.0001

    # 将角度转换为弧度[0, 2Π]
    radians = to_radians(normalize_angle(number))

    # 计算 cos(x) 直到达到指定的误差限制
    cos_approx = cos_taylor(radians, error_limit)

    # 限制值域在 [-1, 1] 内
    cos_approximation = max(-1, min(cos_approx, 1))

    return cos_approximation
