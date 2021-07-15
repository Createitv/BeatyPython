#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 16:06:10
# Theme :
from abc import ABCMeta, abstractmethod


class WaterHeater:
    """热水器"""

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是:" + str(self.__temperature) + "C")
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """洗澡模式和饮用模式的父类"""

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            print("水温度正好,可以来洗澡了")


class DrinkingMode(Observer):
    """饮用模式"""

    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！ 可以饮用了")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


testWaterHeater()