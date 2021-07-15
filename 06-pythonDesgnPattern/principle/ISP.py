#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 14:57:38
# Theme : 接口隔离原则

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def features(self):
        pass

    @abstractmethod
    def moving(self):
        pass


class IRunnable(metaclass=ABCMeta):
    """奔跑的接口"""

    @abstractmethod
    def running(self):
        pass


class IFlyable(metaclass=ABCMeta):
    """飞行的接口"""

    @abstractmethod
    def flying(self):
        pass


class INatatory(metaclass=ABCMeta):

    @abstractmethod
    def swimming(self):
        pass


class MammalAnimal(Animal, IRunnable):
    """哺乳动物"""

    def __init__(self, name):
        super().__init__(name)

    def features(self):
        print(self._name + "的生理特征：恒温，胎生，哺乳。")

    def running(self):
        print("在陆上跑...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.running()

# cow = MammalAnimal("cow")
# cow.features()


class BirdAnimal(Animal, IFlyable):
    """鸟类动物"""

    def __init__(self, name):
        super().__init__(name)

    def features(self):
        print(self._name + "的生理特征：恒温，卵生，前肢成翅。")

    def flying(self):
        print("在天空飞...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.flying()


class FishAnimal(Animal, INatatory):
    """鱼类动物"""

    def __init__(self, name):
        super().__init__(name)

    def features(self):
        print(self._name + "的生理特征：流线型体形，用鳃呼吸。")

    def swimming(self):
        print("在水里游...")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.swimming()


class Bat(MammalAnimal, IFlyable):
    """蝙蝠"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print("行走功能已经退化。")

    def flying(self):
        print("在天空飞...", end="")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.flying()
        self.running()


class Swan(BirdAnimal, IRunnable, INatatory):
    """天鹅"""

    def __init__(self, name):
        super().__init__(name)

    def running(self):
        print("在陆上跑...", end="")

    def swimming(self):
        print("在水里游...", end="")

    def moving(self):
        print(self._name + "的活动方式：", end="")
        self.running()
        self.swimming()
        self.flying()


class CrucianCarp(FishAnimal):
    """鲫鱼"""

    def __init__(self, name):
        super().__init__(name)


def testAnimal():
    bat = Bat("蝙蝠")
    bat.features()
    bat.moving()
    swan = Swan("天鹅")
    swan.features()
    swan.moving()
    crucianCarp = CrucianCarp("鲫鱼")
    crucianCarp.features()
    crucianCarp.moving()


testAnimal()
