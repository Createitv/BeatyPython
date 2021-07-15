#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 08:32:08
# Theme : 单例模式2

class MyBeautifulGril:
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + ",我一件钟情")
            MyBeautifulGril._isFirstInit = True
        else:
            print("遇见" + name + "我置若罔闻!")

    def showMyHeart(self):
        print(self.__name + "你就是我心中的唯一!")


def testLove():
    jenny = MyBeautifulGril("jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))

# testLove()

# 单例实现一


class Singleton1(object):
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            self.__isFirstInit = True

    def getName(self):
        return self.__name


def test():
    tony = Singleton1("Tony")
    karry = Singleton1("karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry", tony == karry)

# test()


class Singleton2(type):
    """单例实现方式二"""

    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None  # 初始化全局变量cls._instance为None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程，如果cls._instance为None则创建，否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class CustomClass(metaclass=Singleton2):
    """用户自定义的类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


def test():
    tony = CustomClass("Tony")
    karry = CustomClass("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry:", tony == karry)
# test()


def singletonDecorator(cls, *args, **kwargs):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


@singletonDecorator
class Singleton3():
    """单例模式实现三"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

def test():
    tony = Singleton3("Tony")
    karry = Singleton3("karry")
    print(tony.getName(), karry.getName())
    print("id(tony):", id(tony), "id(karry):", id(karry))
    print("tony == karry", tony == karry)
test()
