def loop_sum(lst):
    if lst == []:
        return 0
    return lst[0] + loop_sum(lst[1:])


def number(lst):
    if lst == []:
        return 0
    return 1 + number(lst[1:])


def max_(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


def binary(l, num):
    print(l)
    if len(l) == 1:
        if l[0] == num:
            print("I find it here")
        else:
            print("Doesn't exist")
        return
    else:
        mid_index = len(l) // 2
        mid_value = l[mid_index]
        if mid_value == num:
            print("I find it")
            return
        if mid_value > num:
            l = l[:mid_index]
        else:
            l = l[mid_index:]
    binary(l, num)


l = [1, 2, 3, 4, 5, 6]
# print(loop_sum(l))
# print(number(l))
# print(max_(l))
print(binary(l, 20))