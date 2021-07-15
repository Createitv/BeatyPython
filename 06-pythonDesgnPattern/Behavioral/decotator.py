#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 19:26:43
# Theme : 装饰器模式

from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装:")


class Engineer(Person):

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getskill(self):
        return self.__skill

    def wear(self):
        print("我是" + self.getskill() + "工程师" + self._name, end=", ")
        super().wear()


class Teacher(Person):

    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
       print("我是" + self._name + self.getTitle(), end=", ")
       super().wear()


class ClothingDecorator(Person):

    def __init__(self, person):
        self._decorator = person

    def wear(self):
        self._decorator.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条卡其色裤子")


class BeltDecorator(ClothingDecorator):

    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条黑色腰带") 
    
class LeatherShoesDecorator(ClothingDecorator):
    
    def __init__(self, person):
        super().__init__(person)
    
    def decorate(self):
        print("一双深色休闲皮鞋")
    
class KnittedSweaterDecorator(ClothingDecorator):
    
    def __init__(self, person):
        super().__init__(person)
    
    def decorate(self):
        print("一件紫色毛衣") 
    
class WhiteShirtDecorator(ClothingDecorator):
    
    def __init__(self, person):
        super().__init__(person)
    
    def decorate(self):
        print("一件毛色寸衫")
    
class GlassesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)
    
    def decorate(self):
        print("一副黑色眼镜框")

def testDecorator():
    tony = Engineer("Tony", "客户端")
    pant = CasualPantDecorator(tony)
    pant.wear()
    # belt = BeltDecorator(pant)
    # shoes = LeatherShoesDecorator(belt)
    # shirt = WhiteShirtDecorator(shoes)
    # sweater = KnittedSweaterDecorator(shirt)
    # glasses = GlassesDecorator(sweater)
    # glasses.wear()
    decorateTeacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells", "教授"))))
    # decorateTeacher.wear()
testDecorator()
