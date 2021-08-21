from copy import deepcopy


def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result


def find_product(lst):
    array = []
    for i in range(len(lst)):
        new_lst = deepcopy(lst)
        new_lst.remove(lst[i])
        array.append(product(new_lst))
    return array


print(find_product([1, 2, 3, 4]))
print(find_product([2, 5, 9, 3, 6]))
