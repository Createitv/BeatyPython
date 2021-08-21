def test_var_args(f_arg, *argv):
    """
    >>> test_var_args('yasoob', 'python', 'eggs', 'test')
    first normal arg: yasoob
    another arg through *argv: python
    another arg through *argv: eggs
    another arg through *argv: test
    """
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


def greet_me(**kwargs):
    """
    >>> greet_me(name='yasoob')
    name = yasoob
    """
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test_args_kwargs(arg1, arg2, arg3):
    """
    >>> args = ("two", 3, 5)
    >>> test_args_kwargs(*args)
    arg1: two
    arg2: 3
    arg3: 5
    >>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    >>> test_args_kwargs(**kwargs)
    arg1: 5
    arg2: two
    arg3: 3
    """
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def test(arg1, *args):
    """
    >>> test("name", "title", "description")
    arg1: name title description
    """
    print("arg1:", arg1, *args)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
