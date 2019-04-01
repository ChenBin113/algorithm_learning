def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        standard = lst[0]
        smaller = [i for i in lst[1:] if i < standard]
        bigger = [i for i in lst[1:] if i > standard]
        return quicksort(smaller) + [standard] + quicksort(bigger)


l = [1, 34, 4, 2, 5, 256, 23]
print(quicksort(l))