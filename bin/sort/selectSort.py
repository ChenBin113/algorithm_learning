"""
选择排序
1. 从头开始比较得原数列中最小数
2. 赋值给新数列，删除原数列中最小数
3. 循环直到原数列为空
"""


def choose_small(list_1):
    smallest = list_1[0]
    smallest_index = 0
    for i in range(1, len(list_1)):
        if smallest > list_1[i]:
            smallest = list_1[i]
            smallest_index = i
    return smallest_index


def new_list(list_1):
    list_new = []
    for j in range(len(list_1)):
        temp_index = choose_small(list_1)
        # list_new.append(list_1[temp_index])
        # list_1.pop(temp_index)
        list_new.append(list_1.pop(temp_index))  # pop返回的是删除项
    return list_new


if __name__ == '__main__':
    lis = [1, 5, 4]
    print(new_list(lis))
