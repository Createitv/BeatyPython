class OddContainer():
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2 == 0:
            return False
        return True


odd_container = OddContainer()
for x in range(10):
    print(x, x in odd_container)
