"""  向文件输出“奋斗成就更好的你”  """
filename = "案例1.txt"

"""方式1"""
file = open(filename, "w+")
print("奋斗成就更好的你", file=file)

"""方式2，使用文件读写操作"""
with open(filename, "a+") as file:  # 追加
    file.write("奋斗成就更好的你2")
