#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 11:40:45
# Theme : 抽象工厂模式
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

"""Implementation of the abstract factory pattern"""
import abc
import random


class Solider(object):

    def __init__(self, gun, buttle):
        self.gun = gun
        self.buttle = buttle

    def fire(self):
        self.gun.pong()
        self.buttle.pa()


class Gunfactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_gun(self):
        pass

    @abc.abstractmethod
    def get_bullet(self):
        pass


class Gun(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def pong(self):
        pass


class Bullet(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def pa(self):
        pass


class Rifle(Gun):

    def pong(self):
        print("Rifle fire,pong!")


class Handgun(Gun):

    def pong(self):
        print("Handgun fire,pong,pong,pong")


class RifleBullet(Bullet):

    def pa(self):
        print("Rifle buttle,pa!")


class HandgunBullet(Bullet):

    def pa(self):
        print("Handgun buttle,pa,pa,pa")


class RifleFactory(Gunfactory):

    def get_gun(self):
        return Rifle()

    def get_bullet(self):
        return RifleBullet()


class HandgunFactory(object):

    def get_gun(self):
        return Handgun()

    def get_bullet(self):
        return HandgunBullet()


if __name__ == "__main__":
    rifle_factory = RifleFactory()
    handgun_factory = HandgunFactory()
    factories = [rifle_factory, handgun_factory]
    for i in range(4):
        factory = random.choice(factories)
        gun = factory.get_gun()
        bullet = factory.get_bullet()
        solider = Solider(gun, bullet)
        solider.fire()
        print("=" * 20)

### OUTPUT ###
# Rifle fire,pong!
# Rifle buttle,pa!
# ====================
# Handgun fire,pong,pong,pong
# Handgun buttle,pa,pa,pa
# ====================
# Handgun fire,pong,pong,pong
# Handgun buttle,pa,pa,pa
# ====================
# Rifle fire,pong!
# Rifle buttle,pa!
# ====================
