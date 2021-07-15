from abc import ABCMeta, abstractmethod

# ------抽象的产品------


class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class PhoneCPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class PhoneOS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# ------具体的产品------


class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通手机小手机壳')


class BigShell(PhoneShell):
    def show_shell(self):
        print('普通手机大手机壳')


class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')


class SnapDragonCPU(PhoneCPU):
    def show_cpu(self):
        print('骁龙CPU')


class HuaweiCPU(PhoneCPU):
    def show_cpu(self):
        print('华为CPU')


class AppleCPU(PhoneCPU):
    def show_cpu(self):
        print('苹果CPU')


class AndroidOS(PhoneOS):
    def show_os(self):
        print('IOS系统')


class AppleOS(PhoneOS):
    def show_os(self):
        print('安卓系统')

# ------抽象的工厂------


class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# ------具体的工厂------


class HuaweiFactory(PhoneFactory):
    def make_shell(self):
        return SmallShell()

    def make_cpu(self):
        return HuaweiCPU()

    def make_os(self):
        return AndroidOS()


class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return AppleOS()

# ------客户端------


class Phone:
    def __init__(self, shell, cpu, os):
        self.shell = shell
        self.cpu = cpu
        self.os = os

    def show_info(self):
        print('手机信息：')
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()


def make_phone(factory):
    shell = factory.make_shell()
    cpu = factory.make_cpu()
    os = factory.make_os()
    return Phone(shell, cpu, os)


p = make_phone(HuaweiFactory())
p.show_info()
"""
手机信息：
普通手机小手机壳
化为CPU
IOS系统
"""
