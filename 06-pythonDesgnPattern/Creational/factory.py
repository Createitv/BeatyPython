#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/05 17:34:24
# Theme : 简单工厂设计模式,工厂是创建其他产品类型的类


# ---------例子一---------------
class Mercedes():
    def __repr__(self):
        return "Mercedes-Benz"


class Bmw():
    def __repr__(self):
        return "BMW"


class Audi():
    def __repr__(self):
        return "Audi A8"


class SimpleCarFactory():
    """简单工厂
    """
    @staticmethod
    def product_car(name):
        if name == "mb":
            return Mercedes()
        elif name == "bmw":
            return Bmw()
        elif name == "audi":
            return Audi()


def test():
    c1 = SimpleCarFackproduct_car("mb")
    c2 = SimpleCarFactory.product_car("bmw")
    c3 = SimpleCarFactory.product_car("audi")

    print(c1, c2, c3)


# -----------例子2--------------------
from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    """抽象产品角色"""

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    @abstractmethod
    def getResult(self):
        pass


class Add(Operation):
    """具体产品角色"""

    def getResult(self):
        return self.first_num + self.second_num


class Sub(Operation):
    """具体产品角色"""

    def getResult(self):
        return self.first_num - self.second_num


class Mul(Operation):
    """具体产品角色"""

    def getResult(self):
        return self.first_num * self.second_num


class Div(Operation):
    """具体产品角色"""

    def getResult(self):
        try:
            return 1.0 * self.first_num / self.second_num
        except ZeroDivisionError:
            raise


class OperationFactory(object):
    """产品工厂角色"""

    def __init__(self, operation):
        self.op = operation

    def chooseOpertator(self):
        if self.op == "+":
            return Add
        elif self.op == "-":
            return Sub
        elif self.op == "*":
            return Mul
        elif self.op == "/":
            return Div


def test():
    operator = OperationFactory("*").chooseOpertator()

    # operator.first_num = 4
    # operator.second_num = 5
    # print(operator == Add())
    print(operator(3, 4).getResult())


# test()


# ---------------例子3------------------
class Coffee(metaclass=ABCMeta):
    """咖啡类,抽象产品"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass


class LatteCaffe(Coffee):
    """拉铁咖啡, 具体产品"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "轻柔而香纯"


class MochaCoffee(Coffee):
    """摩卡咖啡, 具体产品"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "丝滑与醇厚"


class Coffeemaker:
    """咖啡机"""

    @staticmethod
    def makeCoffee(coffeeBean):
        "通过staticmethod装饰器修饰来定义一个静态方法"
        if(coffeeBean == "拿铁咖啡豆"):
            coffee = LatteCaffe("拿铁咖啡")
        elif(coffeeBean == "摩卡咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError("不支持的参数：%s" % coffeeBean)
        return coffee


def testCoffeeMaker():
    latte = Coffeemaker.makeCoffee("拿铁咖啡豆")
    print("%s已为您准备好了，口感：%s。请慢慢享用！" % (latte.getName(), latte.getTaste()))
    mocha = Coffeemaker.makeCoffee("摩卡咖啡豆")
    print("%s已为您准备好了，口感：%s。请慢慢享用！" % (mocha.getName(), mocha.getTaste()))

# testCoffeeMaker()


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from enum import Enum
# Python3.4 之后支持枚举Enum的语法


class PenType(Enum):
    """画笔类型"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """画笔"""

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def getType(self):
        pass

    def getName(self):
        return self.__name


class LinePen(Pen):
    """直线画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine


class RectanglePen(Pen):
    """矩形画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """椭圆画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """画笔工厂类"""

    def __init__(self):
        "定义一个字典(key:PenType，value：Pen)来存放对象,确保每一个类型只会有一个对象"
        self.__pens = {}

    def getSingleObj(self, penType, name):
        """获得唯一实例的对象"""

    def createPen(self, penType):
        """创建画笔"""
        if (self.__pens.get(penType) is None):
            # 如果该对象不存在，则创建一个对象并存到字典中
            if penType == PenType.PenTypeLine:
                pen = LinePen("直线画笔")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("矩形画笔")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("椭圆画笔")
            else:
                pen = Pen("")
            self.__pens[penType] = pen
        # 否则直接返回字典中的对象
        return self.__pens[penType]


def testPenFactory():
    factory = PenFactory()
    linePen = factory.createPen(PenType.PenTypeLine)
    print("创建了 %s，对象id：%s， 类型：%s" %
          (linePen.getName(), id(linePen), linePen.getType()))
    rectPen = factory.createPen(PenType.PenTypeRect)
    print("创建了 %s，对象id：%s， 类型：%s" %
          (rectPen.getName(), id(rectPen), rectPen.getType()))
    rectPen2 = factory.createPen(PenType.PenTypeRect)
    print("创建了 %s，对象id：%s， 类型：%s" %
          (rectPen2.getName(), id(rectPen2), rectPen2.getType()))
    ellipsePen = factory.createPen(PenType.PenTypeEllipse)
    print("创建了 %s，对象id：%s， 类型：%s" %
          (ellipsePen.getName(), id(ellipsePen), ellipsePen.getType()))


# testCoffeeMaker()
# testPenFactory()

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付{}元".format(money))


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付{}元".format(money))


class JdPay(Payment):
    def pay(self, money):
        print("京东支付{}元".format(money))


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def createPayment(self):
        pass


class AlipayFactory(PaymentFactory):
    def createPayment(self):
        return Alipay()


class WechatFactory(PaymentFactory):
    def createPayment(self):
        return WechatPay()


class JdFactory(PaymentFactory):
    def createPayment(self):
        return JdPay()

def test()
    hfp = AlipayFactory().createPayment()
    hfp.pay(10)
    hfp = WechatFactory().createPayment()
    hfp.pay(10)
    hfp = JdFactory().createPayment()
    hfp.pay(10)
test()