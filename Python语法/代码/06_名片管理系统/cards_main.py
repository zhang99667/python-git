#   #！ she-ban
import cards_tools

isRun = True  # 控制菜单是否循环显示
while isRun:

    # 显示菜单
    cards_tools.menu()

    choose = input("请选择操作功能：")
    print("您选择的操作为【%s】" % choose)
    # 判断输入的字符是否属于菜单中所显示的字符
    if choose in ["1", "2", "3", "q", "Q"]:

        # 'Q'或'q'：退出系统
        if choose == "q" or choose == "Q":
            isRun = False

        # '1'：新建名片
        elif choose == "1":
            # 如果在开发程序时，不希望立刻编写分支内部的代码
            # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确
            # 程序运行时，pass 关键字不会执行任何操作
            cards_tools.new_card()

            pass

        # '2'：显示全部
        elif choose == "2":
            cards_tools.show_all()

        # '3'：查询名片
        elif choose == "3":
            cards_tools.search_card()

    # 其他字符：输入的字符不在菜单范围内
    else:
        print("输入有误，请重新输入！")
