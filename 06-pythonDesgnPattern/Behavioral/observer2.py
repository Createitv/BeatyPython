from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者基类"""
    @abstractmethod
    def update(self, observer, object):
        pass


class Observable:
    """被观察的基类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        """添加所有观察者，自动调用update()更新状态"""
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """观察对象: 热水器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度为:" + str(self.__temperature) + "C")
        self.notifyObservers()


class WashingMode(Observer):
    """洗澡模式"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水温刚好适合洗澡")


class DrinkingMode(Observer):
    """饮用模式"""
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已经烧开！可以放心饮用")
            

def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)
if __name__ == '__main__':
    testWaterHeater()