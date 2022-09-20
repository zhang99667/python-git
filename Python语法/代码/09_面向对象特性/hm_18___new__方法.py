class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1. 创建对象时，new 方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间，并返回
        return super().__new__(cls)

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
