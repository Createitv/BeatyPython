
# 构造最小堆
class MinHeap():
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.array = [None] * maxSize
        self._count = 0

    def length(self):
        return self._count

    def show(self):
        if self._count <= 0:
            print('null')
        print(self.array[: self._count], end=', ')

    def add(self, value):
        # 增加元素
        if self._count >= self.maxSize:
            raise Exception('The array is Full')
        self.array[self._count] = value
        self._shift_up(self._count)
        self._count += 1

    def _shift_up(self, index):
        # 比较结点与根节点的大小， 较小的为根结点
        if index > 0:
            parent = (index - 1) // 2
            if self.array[parent] > self.array[index]:
                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                self._shift_up(parent)

    def extract(self):
        # 获取最小值，并更新数组
        if self._count <= 0:
            raise Exception('The array is Empty')
        value = self.array[0]
        self._count -= 1  # 更新数组的长度
        self.array[0] = self.array[self._count]  # 将最后一个结点放在前面
        self._shift_down(0)

        return value

    def _shift_down(self, index):
        # 此时index 是根结点
        if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            # 判断左右结点是否越界，是否小于根结点，如果是这交换
            if left < self._count and right < self._count and self.array[left] < self.array[index] and self.array[left] < self.array[right]:
                # 交换得到较小的值
                self.array[index], self.array[left] = self.array[left], self.array[index]
                self._shift_down(left)
            elif left < self._count and right < self._count and self.array[right] < self.array[left] and self.array[right] < self.array[index]:
                self.array[right], self.array[index] = self.array[index], self.array[right]
                self._shift_down(right)

            # 特殊情况： 如果只有做叶子结点
            if left < self._count and right > self._count and self.array[left] < self.array[index]:
                self.array[left], self.array[index] = self.array[index], self.array[left]
                self._shift_down(left)


if __name__ == '__main__':
    import random
    m = MinHeap(10)
    num = [random.choice(range(1, 100)) for i in range(9)]
    print(m.length())
    for i in num:
        m.add(i)
    m.show()
    print(m.length())
    for i in range(5):
        print(m.extract(), end=' ')
