#!/Users/tnt/Documents/虚拟环境/Django/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/06/06 10:12:03
# Theme : 基于工厂方法的语言本地化

class GreekLocalizer():

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        # 过去翻译，默认值为初始值
        return self.translations.get(msg, msg)


class EnglishLocalizer():

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") ->object:
    localizer = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizer[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")
    
    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # for msg in "dog parrot cat bear".split():
    #     print(e.localize(msg), g.localize(msg))
