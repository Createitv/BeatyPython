# class Player:
#     "单例模式"
#     # 类变量实例化之前为None
#     __instance = None
#     # 创建flag,无论实例化几次只有一次__init__
#     __flag = False

#     def __new__(cls, *args, **kwargs):
#         # 只允许实例化一次
#         if cls.__instance == None:
#             print("New 执行了")
#             # super()继承object的__new__方法
#             cls.__instance = super().__new__(cls)

#         # 返回实例化之后的对象而不是cls
#         return cls.__instance

#     def __init__(self):
#         if not Player.__flag:
#             print("init执行了")
#             Player.__flag = True


# video = Player()
# print(video)

# print(video._Player__instance)
# music = Player()
# print(music)
# print(video._Player__instance)
# print(Player.__dict__)
# print(video.__dict__)

class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("******My int", args)
        print("*****Do with these objects")
        return type.__call__(cls,*args,**kwargs)

class int(metaclass = MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
i = int(4, 5)