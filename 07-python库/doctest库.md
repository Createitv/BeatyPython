这个 [`doctest`](https://www.osgeo.cn/cpython/library/doctest.html#module-doctest) 模块搜索看起来像交互式Python会话的文本片段，然后执行这些会话以验证它们是否如图所示工作。使用doctest有几种常见方法：

- 通过验证所有交互式示例是否仍按文档方式工作来检查模块的docstring是否是最新的。
- 通过验证来自测试文件或测试对象的交互示例是否按预期工作来执行回归测试。
- 为一个包编写教程文档，用输入输出示例充分说明。这取决于是否强调示例或说明性文本，具有“识字测试”或“可执行文档”的味道。

下面是一个完整但很小的示例模块：

```python
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

如果你运行 `example.py` 直接从命令行， [`doctest`](https://www.osgeo.cn/cpython/library/doctest.html#module-doctest) 发挥其魔力：

```
$ python example.py
```

没有输出！这很正常，意味着所有的例子都有效。通过 `-v` 到脚本，以及 [`doctest`](https://www.osgeo.cn/cpython/library/doctest.html#module-doctest) 打印一个详细的日志，记录它正在尝试的内容，并在结尾打印一个摘要：

```
$ python example.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    [factorial(n) for n in range(6)]
Expecting:
    [1, 1, 2, 6, 24, 120]
ok
```

以此类推，最终以：

```bash
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
        ...
    OverflowError: n too large
ok
2 items passed all tests:
   1 tests in __main__
   8 tests in __main__.factorial
9 tests in 2 items.
9 passed and 0 failed.
Test passed.
$
```

你只需要知道这些就可以开始有效利用 [`doctest`](https://www.osgeo.cn/cpython/library/doctest.html#module-doctest) ！跳进去。以下部分提供了完整的详细信息。请注意，标准的Python测试套件和库中有许多doctest示例。在标准测试文件中可以找到特别有用的示例 `Lib/test/test_doctest.py` .