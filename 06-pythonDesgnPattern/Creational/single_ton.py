#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/05 15:28:45
# Theme : 单例模式


# class Player:
#     def __init__(self):
# class Player:
#     def __init__(self):
#         print("对象__init__开始")


# viedo = Player()
# print(viedo)
# music = Player()
# print(music)
# 每次创建对象都新开辟一块地址


# class Player:
#     def __new__(cls, *args, **kwargs):
#         print("__new__执行")

#     def __init__(self):
#         print("对象__init__开始")


# viedo = Player()
# print(viedo)
# music = Player()
# print(music)
# __new__未返回对象,对象地址为空

class Player:

    # 类变量实例化之前为None
    __instance = None
    # 创建flag,无论实例化几次只有一次__init__
    __flag = False

    def __new__(cls, *args, **kwargs):
        # 只允许实例化一次
        if cls.__instance == None:
            print("New 执行了")
            # super()继承object的__new__方法
            cls.__instance = super().__new__(cls)

        # 返回实例化之后的对象而不是cls
        return cls.__instance

    def __init__(self):
        if not Player.__flag:
            print("init执行了")
            Player.__flag = True


# video = Player()
# print(video)
# music = Player()
# print(music)
# print(hasattr(video, "_Player__instance")) # true
# print(hasattr(video, "a"))                          #true
# print(hasattr(video, "_Player__flag"))


# 更简单的写法
# ---------------------------推荐使用---------------------------------
class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# s = Singleton()
# print("Obejct Creage:", s)
# s1 = Singleton()
# print("Obejct Creage:", s1)


# 懒汉实例化

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called....")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

# s = Singleton()
# print("Obejct Create:", Singleton.getInstance())
# s1 = Singleton()

# 元类的单例实现


class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class Logger(metaclass=MetaSingleton):
    pass

# loggwer1 = Logger()
# loggwer2 = Logger()
# print(loggwer1, loggwer2)


import sqlite3


class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Obj Db1", db1)
print("Database Obj Db2", db2)
