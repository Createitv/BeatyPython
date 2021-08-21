def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


test_lst = [1, 2, 3, 34, 4, 325, 5, 23, 3121]
print(sequentialSearch(test_lst, 13))
print(sequentialSearch(test_lst, 34))
