# list comprehension
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# dict comprehension
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)

# set comprehension
squared = {x**2 for x in [1, 1, 2]}
print(squared)

# generate comprehension
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
