#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 13:49:40
# Theme : 构建模式,也叫生成器模式
from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    """玩具"""

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "个"):
        self.__components.append([component, count, unit])
        print("%s 增加了 %d %s%s" % (self._name, count, unit, component) );

    @abstractmethod
    def feature(self):
        pass


class Car(Toy):
    """小车"""

    def feature(self):
        print("我是 %s，我可以快速奔跑……" % self._name)


class Manor(Toy):
    """庄园"""

    def feature(self):
        print("我是 %s，我可供观赏，也可用来游玩！" % self._name)


class ToyBuilder:
    """玩具构建者"""

    def buildCar(self):
        car = Car("迷你小车")
        print("正在构建 %s ……" % car.getName())
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘")
        return car

    def buildManor(self):
        manor = Manor("淘淘小庄园")
        print("正在构建 %s ……" % manor.getName())
        manor.addComponent('客厅', 1, "间")
        manor.addComponent('卧室', 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1, "个")
        manor.addComponent("围墙", 1, "堵")
        return manor


# Test
#==============================
def testBuilder():
    builder = ToyBuilder()
    car = builder.buildCar()
    car.feature()

    print()
    mannor = builder.buildManor()
    mannor.feature()

#---------------例2---------------------
# testBuilder()
import abc
import time


class Dish(object):

    def __init__(self):
        self.ginger_onion = None
        self.salt = None
        self.edible_oil = None
        self.vegetables = None

    def __str__(self):
        return 'dish including %s_%s_%s_%s' % (self.ginger_onion, self.edible_oil, self.vegetables, self.salt)


class Abstract_builder(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_edible_oil(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def add_ginger_onion(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def add_vegetables(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def add_salt(self, *args, **kwargs):
        pass


class Tomatoes_dish_builder(Abstract_builder):
    def __init__(self):
        self.dish = Dish()

    def add_edible_oil(self):
        self.dish.edible_oil = '地沟油'
        time.sleep(1)
        return self

    def add_ginger_onion(self):
        self.dish.ginger_onion = '老姜和大葱'
        time.sleep(1)
        return self

    def add_vegetables(self):
        self.dish.vegetables = '番茄'
        time.sleep(1)
        return self

    def add_salt(self):
        self.dish.salt = '海盐'
        time.sleep(1)
        print('tomatoes dish is ready')
        return self


class Potato_dish_builder(Abstract_builder):
    def __init__(self):
        self.dish = Dish()

    def add_edible_oil(self):
        self.dish.edible_oil = '菜子油'
        time.sleep(1)
        return self

    def add_ginger_onion(self):
        self.dish.ginger_onion = '生姜和小葱'
        time.sleep(1)
        return self

    def add_vegetables(self):
        self.dish.vegetables = '新土豆'
        time.sleep(1)
        return self

    def add_salt(self):
        self.dish.salt = '加典盐'
        time.sleep(1)
        print('potato dish is ready')
        return self


class Director(object):
    def __init__(self):
        self.builder = None

    def build(self, builder):
        self.builder = builder
        self.builder.\
            add_edible_oil().\
            add_ginger_onion().\
            add_vegetables().\
            add_salt()
        return self.builder.dish


if __name__ == '__main__':
    tomato_builder = Tomatoes_dish_builder()
    potato_builder = Potato_dish_builder()
    director = Director()
    tomato_dish = director.build(tomato_builder)
    print(tomato_dish)
    potato_dish = director.build(potato_builder)
    print(potato_dish)
