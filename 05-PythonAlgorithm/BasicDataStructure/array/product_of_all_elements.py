#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/25 21:53:46
# Theme : 除了本身其他列表内的元素和

def find_product_1(lst):
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i + 1:]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


def find_product(lst):
    """The algorithm for this solution is to first create a new list with products of all elements to the left of each element as done on lines 4-6. Then multiply each element in that list to the product of all the elements to the right of the list by traversing it in reverse as done on lines 9-11
    先乘以数组所有左边元素，再乘当前元素所有右边元素，复杂度O(n)
    """
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product


# print(find_product([0, 1, 2, 3]))
print(find_product([1, 2, 3, 4]))
