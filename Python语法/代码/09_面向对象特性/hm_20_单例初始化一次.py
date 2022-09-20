class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1. 判断是否执行过初始化动作
        if not MusicPlayer.init_flag:
            # 2. 没有执行过，执行初始化动作
            print("初始化会被调用")
            # 3. 修改类属性的标记
            MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)
