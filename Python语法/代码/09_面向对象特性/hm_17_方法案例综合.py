class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_names = player_name

    # 类方法，显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分：", cls.top_score)

    # 静态方法，显示游戏帮助信息
    @staticmethod
    def show_help():
        print("Help information：good good study day day up")

    # 实例方法，开始当前玩家的游戏
    def start_game(self):
        print(self.player_names, "开始游戏")


# 静态方法和类方法都是通过 类名. 的方式访问
# 1. 查看帮助信息
Game.show_help()
# 2. 查看历史最高分
Game.show_top_score()


# 3. 开始游戏
game = Game("nancy")
game.start_game()
