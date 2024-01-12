# 本次实验的目的是 产生随机数并排序

import random


# 生成ranges范围内的num个整数 指定了默认值
def random_int(ranges=None, num=1):
    # 首先判断范围列表是否正确
    if ranges is None:
        ranges = [0, 100]
    if ranges[0] > ranges[1]:
        print("第一个值应当小于等于第二个值")
        return []
    # 生成num个随机数
    res = []
    for item in range(num):
        res.append(random.randint(ranges[0], ranges[1] + 1))
    return res


# 生成ranges范围内的num个小数 制定默认值
def random_float(ranges=None, num=1):
    if ranges is None:
        ranges = [0, 100]
    if ranges[0] > ranges[1]:
        print("第一个值应当小于等于第二个值")
        return []
    res = []
    for item in range(num):
        res.append(random.random() * (ranges[1] - ranges[0]) + ranges[0])
    return res


# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [item for item in arr[1:] if item <= pivot]
        greater = [item for item in arr[1:] if item > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    int_list = random_int([20, 60], 5)
    float_list = random_float([20.1, 60], 5)
    int_list_sort = quick_sort(int_list)
    float_list_sort = quick_sort(float_list)

    print('整数列表排序前：', int_list)
    print('整数列表排序前：', int_list_sort)
    print('浮点列表排序前：', float_list)
    print('浮点列表排序前：', float_list_sort)
