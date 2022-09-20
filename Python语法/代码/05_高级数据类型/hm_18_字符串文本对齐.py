# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
poem = ["登鹊雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千限目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10,"　")) # 居中对齐
    # print("|%s|" % poem_str.ljust(10,"　")) # 左对齐
    # print("|%s|" % poem_str.rjust(10, "　"))  # 右对齐
