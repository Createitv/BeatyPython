#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/08 21:47:33
# Theme : 适配模式

from abc import ABCMeta, abstractmethod


class SocketEntity():

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self__typeOfPin = typeOfPin


class ISocket(metaclass=ABCMeta):

    def getName(self):
        pass

    def getSocket(self):
        pass


class ChineseSocket(ISocket):
    def getName(self):
        return "国标插头"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:

    def name(self):
        return "英标插座"

    def socketInterface(self):
        return SocketEntity(3, "T字方形")


class AdapterSocket(ISocket):
    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return self.__britishSocket.name() + "转换器"
    
    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket


def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"

    print("[%s]：\n针脚数量：%d，针脚类型：%s； %s中国标准，%s给大陆的电子设备充电！"
          % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))


def testSocket():
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(),
                             chineseSocket.getSocket())

    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(),
                             britishSocket.socketInterface())

    adapterSocket = AdapterSocket(britishSocket)
    canChargeforDigtalDevice(adapterSocket.getName(),
                             adapterSocket.getSocket())

testSocket()