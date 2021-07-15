class A():
    def __init__(self, a=3, b=4):
        self.a = a
        self.b = b


class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b


obj = B()
print(obj.a)
