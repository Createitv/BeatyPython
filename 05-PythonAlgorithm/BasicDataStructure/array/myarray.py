#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/12 22:00:30
# Theme : 自定义数组

class MyArray:
    def __init__(self, capacity: int) -> object:
        self._data = []
        self._capacity = capacity

    def __getitem__(self, key: int) -> object:
        return self._data[key]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> int:
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return False
    
    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False
        

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def __str__(self):
        return str(self._data)


def test_myarray():
    array = MyArray(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    print(array)


if __name__ == "__main__":
    test_myarray()
