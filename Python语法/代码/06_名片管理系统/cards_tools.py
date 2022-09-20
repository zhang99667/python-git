# 记录所有名片的字典
card_list = []


def menu():
    print("=" * 50)
    print("欢迎使用【名片管理系统】V1.0".center(40))
    print("1. 新建名片".center(45))
    print("2. 显示全部".center(45))
    print("3. 查询名片".center(45))
    print("Q. 退出系统".center(45))
    print("=" * 50)


def new_card():
    # 提示用户输入名片的详细信息
    # 为了避免混淆，输入信息用 _str 结尾
    name_str = input("请输入姓名：")
    tel_str = input("请输入电话：")
    qq_number_str = input("请输入QQ号：")
    email_str = input("请输入邮箱：")

    # 将信息存储到字典中
    card_dict = {
        "name": name_str,
        "tel": tel_str,
        "qq_number": qq_number_str,
        "email": email_str
    }

    # 向名片字典中追加数据
    card_list.append(card_dict)

    # 提示添加成功
    print("名片%s添加成功" % name_str)


def show_all():
    clear_window()
    print("名片信息如下：")
    print("~" * 50)

    # 判断是否存在名片
    if len(card_list) == 0:
        print("还未创建名片！")
    else:
        # 打印表头
        for title in ["姓名", "电话", "QQ", "Email"]:
            print(title, end="\t\t")

        print()  # 换行
        print("-" * 50)  # 分隔符

        # 打印名片信息
        for card in card_list:
            # 显示字典的 value
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                            card["tel"],
                                            card["qq_number"],
                                            card["email"]))

    print("~" * 50)


def search_card():
    clear_window()

    # 判断是否存在名片
    if len(card_list) == 0:
        print("还未创建名片！")

    else:
        search_name = input("请输入要搜索的名字：")
        print("查询名片信息如下：")
        print("~" * 50)
        for card in card_list:

            if card["name"] == search_name:
                print(card["name"] + "\t\t" + card["tel"] + "\t\t" + card["qq_number"] + "\t\t" + card["email"])
                card_update(card, search_name)
                break

        # 如果没搜索到当前名字
        else:
            print("%s不存在" % search_name)

    print("~" * 50)


# 对名片进行修改和删除
def card_update(card, search_name):
    isRun = True  # 控制菜单是否循环显示
    while isRun:
        choose = input("请选择操作【1.修改 2.删除 q.不做更改】")

        # 判断输入的字符是否存在功能范围内
        if choose not in ["1", "2", "q", "Q"]:
            # 不在范围内，返回至主菜单
            print("输入有误，重新输入！")

        else:
            # 修改名片信息
            if choose == "1":
                card["name"] = input_card_info(card["name"], "请输入姓名")
                card["tel"] = input_card_info(card["tel"], "请输入电话")
                card["qq_number"] = input_card_info(card["qq_number"], "请输入QQ号码")
                card["email"] = input_card_info(card["email"], "请输入email")

            # 删除名片
            elif choose == "2":
                card_list.remove(card)
                print("%s删除成功！" % search_name)
            # 其他情况直接返回主菜单
            isRun = False


# 对输入信息进行判空
def input_card_info(card_value, tip_message):
    """

    :param card_value:
    :param tip_message:
    :return:
    """
    # 输入修改信息
    result_str = input(tip_message)
    # 对用户输入的内容进行判空
    if len(result_str) <= 0:
        return card_value
    else:
        return result_str


# 清空控制台
def clear_window():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
