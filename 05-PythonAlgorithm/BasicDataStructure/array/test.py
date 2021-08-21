def rearrange(lst):
    # Write your code here
    for i in lst:
        if i >= 0:
            lst.remove(i)
            lst.append(i)
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
