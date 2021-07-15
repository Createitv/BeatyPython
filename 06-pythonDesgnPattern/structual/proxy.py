#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 20:45:56
# Theme : 中介代理模式

from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


class TonyReception(ReceiveParcel):

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def receive(self, parcelContent):
        print(f"货物主人: {self.getName()}, 手机号:{self.getPhoneNum()}")
        print(f"接收到一个包裹,包裹内容:{parcelContent}")


class WendyReception(ReceiveParcel):

    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcelContent):
        print(f"我是{self.__receiver.getName()}的盆友, 我来帮他代拿快递")
        if (self.__receiver is not None):
            self.__receiver.receive(parcelContent)
        print(f'代收人{self.getName()}')


def testReceiveParcel():
    tony = TonyReception("Tony", '2132141')
    print("Tony:接收")
    tony.receive("雪地靴")
    print()
    print("Wendy代收")
    wendy = WendyReception("wendy", tony)
    wendy.receive("雪地靴")

# testReceiveParcel()

# -----------------代理模式框架--------------------------------


class Subject(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content=''):
        pass


class RealSubject(Subject):

    def request(self, content):
        print("RealSubject todo something.....")


class ProxySubject(Subject):
    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content=''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")

def testProxy():
    realObj = RealSubject("RealSubject")
    proxyObj = ProxySubject("ProxySubject", realObj)
    proxyObj.request()

testProxy()