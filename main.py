# 三角函数计算系统测试程序
# 测试精度0.0001
import math
import random
import Arctan
import Arcsin
import Cos
import Sin


def test_sin():
    array = []
    cor = 0
    err = 0
    for _ in range(1000):
        # 生成1000个(0,360)的随机数
        array.append(random.uniform(0, 360))
    for i in range(1000):
        sys_value = Sin.sin(array[i])
        # 将角度转换成弧度
        array[i] = math.pi*(array[i]/180)
        lib_value = math.sin(array[i])
        if abs(lib_value - sys_value) < 0.0001:
            cor = cor + 1
        else:
            err = err + 1
    acc = cor/(cor + err)
    return acc


def test_cos():
    array = []
    cor = 0
    err = 0
    for _ in range(1000):
        # 生成1000个(0,360)的随机数
        array.append(random.uniform(0, 360))
    for i in range(1000):
        sys_value = Cos.cos(array[i])
        # 将角度转换成弧度
        array[i] = math.pi * (array[i] / 180)
        lib_value = math.cos(array[i])
        if abs(lib_value - sys_value) < 0.0001:
            cor = cor + 1
        else:
            err = err + 1
    acc = cor/(cor + err)
    return acc


def test_arcsin():
    array = []
    cor = 0
    err = 0
    for _ in range(1000):
        # 生成1000个(-1,1)的随机数
        array.append(random.uniform(-1, 1))
    for i in range(1000):
        # 将库函数计算出的弧度值转换成角度
        lib_value = 180*math.asin(array[i])/math.pi
        sys_value = Arcsin.arcsin(array[i])
        if abs(lib_value - sys_value) < 0.0001:
            cor = cor + 1
        else:
            err = err + 1
    acc = cor/(cor + err)
    return acc


def test_arctan():
    array = []
    cor = 0
    err = 0
    for _ in range(1000):
        # 生成1000个(-1,1)的随机数
        array.append(random.uniform(-10e6, 10e6))
    for i in range(1000):
        # 将库函数计算出的弧度值转换成角度
        lib_value = 180*math.atan(array[i])/math.pi
        sys_value = Arctan.arctan(array[i])
        if abs(lib_value - sys_value) < 0.0001:
            cor = cor + 1
        else:
            err = err + 1
    acc = cor/(cor + err)
    return acc


if __name__ == '__main__':
    print('Sin accuracy:', test_sin())
    print('Cos accuracy:', test_cos())
    print('Arcsin accuracy:', test_arcsin())
    print('Arctan accuracy:', test_arctan())




