#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 21:09:03
# Theme : 外观模式,门面模式
# 用一个接口封装一个复制的系统

class Register:

    def register(self, name):
        print('活动中心: %s同学报道成功' % name)


class Payment:
    def pay(self, name, money):
        print(f"缴费中心收到{name}同学{money}元付款，缴费成功")


class DormitoryManagermentCenter:
    def provideLivingGoods(self, name):
        print("生活中心:%s同学的生活用品已发送" % name)


class Dormitory:

    def meetRoommate(self, name):
        print('宿舍：' + "大家好，这是刚来的%s同学， 是我们未来四年的室友" % name)


class Volunteer:

    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagermentCenter()
        self.__dormitory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好,%s同学我是志愿者%s,我将带你走完整个报到流程" % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormitory.meetRoommate(name)


def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")


# testRegister()
from os import path
# 引入path，进行路径相关的处理
import logging
# 引入logging，进行错误时的日志记录


class ZIPModel:
    """ZIP模块，负责ZIP文件的压缩与解压
    这里只进行简单模拟，不进行具体的解压缩逻辑"""

    def compress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行“%s”文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("ZIP模块正在进行“%s”文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至“%s”" % dstFilePath)


class RARModel:
    """RAR模块，负责RAR文件的压缩与解压
    这里只进行简单模拟，不进行具体的解压缩逻辑"""

    def compress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行“%s”文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("RAR模块正在进行“%s”文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至“%s”" % dstFilePath)


class ZModel:
    """7Z模块，负责7Z文件的压缩与解压
    这里只进行简单模拟，不进行具体的解压缩逻辑"""

    def compress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行“%s”文件的压缩......" % srcFilePath)
        print("文件压缩成功，已保存至“%s”" % dstFilePath)

    def decompress(self, srcFilePath, dstFilePath):
        print("7Z模块正在进行“%s”文件的解压......" % srcFilePath)
        print("文件解压成功，已保存至“%s”" % dstFilePath)


class CompressionFacade:
    """压缩系统的外观类"""

    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self, srcFilePath, dstFilePath, type):
        """根据不同的压缩类型，压缩成不同的格式"""
        # 获取新的文件名
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath, fullName)
        elif(type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath, fullName)
        elif(type.lower() == "7z"):
            self.__zModel.compress(srcFilePath, fullName)
        else:
            logging.error("Not support this format:" + str(type))
            return False
        return True

    def decompress(self, srcFilePath, dstFilePath):
        """从srcFilePath中获取后缀，根据不同的后缀名(拓展名)，进行不同格式的解压"""
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip"):
            self.__zipModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath, dstFilePath)
        elif(extName.lower() == "7z"):
            self.__zModel.decompress(srcFilePath, dstFilePath)
        else:
            logging.error("Not support this format:" + str(extName))
            return False
        return True


def testCompression():
    facade = CompressionFacade()
    facade.compress("E:\标准文件\生活中的外观模式.md",
                    "E:\压缩文件\生活中的外观模式", "zip")
    facade.decompress("E:\压缩文件\生活中的外观模式.zip",
                      "E:\标准文件\生活中的外观模式.md")
    print()

    facade.compress("E:\标准文件\Python编程——从入门到实践.pdf",
                    "E:\压缩文件\Python编程——从入门到实践", "rar")
    facade.decompress("E:\压缩文件\Python编程——从入门到实践.rar",
                      "E:\标准文件\Python编程——从入门到实践.pdf")
    print()

    facade.compress("E:\标准文件\谈谈我对项目重构的看法.doc",
                    "E:\压缩文件\谈谈我对项目重构的看法", "7z")
    facade.decompress("E:\压缩文件\谈谈我对项目重构的看法.7z",
                      "E:\标准文件\谈谈我对项目重构的看法.doc")
    print()


def testPath():
    filePath = "E:\解析文件\生活中的外观模式——学妹别慌，学长帮你.md"
    dirName = path.dirname(filePath)
    baseName = path.basename(filePath)
    fileName, extName = baseName.split('.')
    fullName = path.join(dirName, fileName + extName)
    i = 0


# testRegister()
testCompression()
# testPath()
