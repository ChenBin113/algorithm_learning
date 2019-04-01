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


l = [1, 2, 3, 4]
print(loop_sum(l))
print(number(l))
print(max_(l))