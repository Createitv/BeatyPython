#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 15:16:55
# Theme : 开闭原则

class Zoo:

    def __init__(self):
        self.__animals = [
            TerrestrialAnimal("狗"),
            AquaticAnimal("鱼")
        ]

    def displayActivity1(self):
        for animal in self.__animals:
            if isinstance(animal, TerrestrialAnimal):
                animal.running()
            else:
                animal.swimming()

    def displayActivity2(self):
        for animal in self.__animals:
            if isinstance(animal, TerrestrialAnimal):
                animal.running()
            elif isinstance(animal, BirdAnimal):
                animal.flying()
            else:
                animal.swimming()


# zoo = Zoo()
# zoo.displayActivity()

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def moving(self):
        pass


class TerrestrialAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在路上跑")


class AquaticAnimal(Animal):
    def __init__(self, name):
        self._name = name

    def moving(self):
        print(self._name + "在水里游....")


class BirdAnimal(Animal):

    def __init__(self, name):
        self._name = name

    def moving(self):
        print(self._name + "在天上飞....")
        
        
class Zoo:
    "动物园"
    def __init__(self):
        self.__animals = []
        
    def addAnimal(self, animal):
        self.__animals.append(animal)
    
    def displayActivity(self):
        print("观察每一种动物的活动方式：")
        for animal in self.__animals:
            animal.moving()


def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("鱼"))
    zoo.addAnimal(BirdAnimal("鸟"))
    zoo.displayActivity()

testZoo()