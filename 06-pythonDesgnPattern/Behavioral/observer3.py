#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 16:32:50
# Theme : 观察者模式版本2
from observer2 import Observable, Observer
import time


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__IsLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "time": time, "region": region})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        ipRegions = {
            "101.47.18.9": "浙江杭州",
            "67.218.147.69": "美国洛杉矶",
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __IsLongDistance(self, name, region):
        lastetRegin = self.__latestRegion.get(name)
        return lastetRegin is not None and lastetRegin != region


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object):
        print("[短信发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] +
              "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print("[邮件发送] " + object["name"] + "您好！检测到您的账户可能登录异常。最近一次登录信息：\n"
              + "登录地区：" + object["region"] +
              "  登录ip：" + object["ip"] + "  登录时间："
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"])))


def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    accout.login("Tony", "67.218.147.69", time.time())

testLogin()