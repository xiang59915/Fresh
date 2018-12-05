# class Game(object):
#
#     # 定义一个类属性 最高分
#     top_score = 0
#
#     # 不需要访问实例属性，也不需要访问类属性 可以定义为静态方法
#     @staticmethod
#     def show_help():
#         print("message of help")
#
#     # 定义一个实例属性
#     def __init__(self, player_name):
#         self.player_name = player_name
#
#     # 定义类方法，调用类属性
#     @classmethod
#     def show_top_score(cls):
#         print("最高分{}".format(cls.top_score))
#
#
#     # 定义实例方法
#     def start_game(self):
#         print("{}开始游戏。。。。。".format(self.player_name))
#
# # 1 首先查看帮助信息
# Game.show_help()
# # 2 查看历史最高分
# Game.show_top_score()
# # 3 创建游戏对象
# xiao = Game("xiaoming")
# xiao.start_game()


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("固定方法单例")
    # 创建new对象时会被自动引用

    # 2 为对象分配空间
    # 可以调用父类方法使用super
        return super().__new__(cls) # new方法是一个静态方法，需要把cls参数传递给这里的new方法对空间的引用
    # 3 返回对象的引用

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)