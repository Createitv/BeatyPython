## 3种编程范式

### 命令式编程

Procedural programming is the most basic form of coding. Code is structured hierarchically into blocks (such as if statements, loops, and functions). It is arguably the simplest form of coding. However, it can be difficult to write and maintain large and complex software due to its lack of enforced structure.

```python
def add_values(any_list):
  sum = 0
  for x in any_list:
      sum += x
  return sum

my_list = [1,2,3,4]
print(add_values(my_list))
```

### 面向对象编程

Object-oriented programming (OOP) structures code into objects. An object typically represents a real item in the program, such as a file or a window on the screen, and it groups all the data and code associated with that item within a single software structure. Software is structured according to the relationships and interactions between different objects. Since objects are encapsulated, with well-defined behavior, and capable of being tested independently, it is much easier to write complex systems using OOP.

```python
class ListOperations(object):
  def __init__(self, any_list):
    self.any_list = any_list

  def add_values(self):
    self.sum = sum(self.any_list)

my_list = [1,2,3,4]
sum_values = ListOperations(my_list)
sum_values.add_values()

print(sum_values.sum)
```

### 函数式编程

Functional programming (FP) uses functions as the main building blocks. Unlike procedural programming, the functional paradigm treats functions as objects that can be passed as parameters, allowing new functions to be built dynamically as the program executes.

Functional programming tends to be more declarative than imperative – your code defines what you want to happen, rather than stating exactly how the code should do it. Some FP languages don’t even contain constructs, such as loops or if statements. However, Python is more general-purpose and allows you to mix programming styles very easily.

```python
import functools
my_list = [1, 2, 3, 4]

# We will look at the functools library later on
sum = functools.reduce(lambda x, y: x + y, my_list)
print(sum)
```

## 函数式编程特点

![image-20210716165537734](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210716165537734.png)

- 纯函数
- 没有副作用
- 函数是第一等公民
- 偏爱不可变对象
- 迭代器胜过不可迭代序列
- 惰性计算
- 避免循环和判断语句
- 递归代替循环
- 高阶函数

## 函数式编程的优缺点

![image-20210716165555625](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210716165555625.png)

### 优点

- 代码更少
- 易读
- Bug更少，更好debug
- Code is potentially mathematically provable
- 易于并行计算多线程

## 缺点

![image-20210716165613576](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210716165613576.png)

- 不可能完全纯函数
- 学习曲线高
- 效率较低，递归消耗大

## 函数式计算

```python
import operator

a=5
b=2

x = operator.add(a, b)       # Equivalent to x = a + b
print(x)

x = operator.truediv(a, b)   # Equivalent to x = a / b 
print(x)

x = operator.floordiv(a, b)  # Equivalent to x = a // b
print(x)

f = partial(operator.add, 3) 
x = f(4) # Equivalent to x = 3 + 7 
print(x)

operator.lt(a, b) # a < b 
operator.eq(a, b) # a == b 
operator.not(a) # not a 
operator.neg(a, b) # -a 
operator.getitem(s, i) # s[i] 
operator.setitem(s, i, x) # s[i] = x 
operator.delitem(s, i) # del s[i]
```

## 生成器

列表推倒式和生成器**内存**比较，生成器内存占用小

```python
import sys
com_lst = [i**2 for i in range(2000)]
print(sys.getsizeof(com_lst))  #16184
gener_lst = (i**2 for i in range(2000))
print(sys.getsizeof(gener_lst)) #112
```

列表推倒式和生成器计算性能比较，生成器计算性能弱

```python
>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
         5 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

>>> cProfile.run('sum((i * 2 for i in range(10000)))')
         10005 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10001    0.002    0.000    0.002    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.001    0.001    0.003    0.003 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

