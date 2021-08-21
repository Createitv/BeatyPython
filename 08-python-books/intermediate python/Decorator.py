from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction

# a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return("Function is running")


can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
