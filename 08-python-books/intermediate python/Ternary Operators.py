condition = True
print(2 if condition else 0)
#Output is 2

print((1, 2)[condition])
#ZeroDivisionError is raised


output = None
msg = output or "No data returned"
print(msg)


def my_function(real_name, optional_display_name=None):
    """
    >>> my_function("John")
    John
    >>> my_function("John", "Mike")
    Mike
    """
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
