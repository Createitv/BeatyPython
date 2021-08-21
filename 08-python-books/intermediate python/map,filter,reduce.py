items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)
# Output: [1, 4, 9, 16, 25]


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# Output: [-5, -4, -3, -2, -1]


from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
# Output: 24
