import os.path

filename = "student.txt"


def menu():
    print("=" * 25, "学生信息管理系统", "=" * 25)
    print("1.录入学生信息")
    print("2.查找学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.排序")
    print("6.统计学生总人数")
    print("7.显示学生信息")
    print("0.退出学生信息管理系统")


def show():
    student_list = []
    student = {}
    with open(filename, "r", encoding="utf-8") as file:
        student_list = file.readlines()
    print("id\tname\tenglish\tpython\tmath")
    for item in student_list:
        d = dict(eval(item))
        id_str = d["id"]
        name_str = d["name"]
        english_str = d["english"]
        python_str = d["python"]
        math_str = d["math"]
        print("%s\t%s\t%s\t\t%s\t\t%s" % (id_str, name_str, english_str, python_str, math_str))


def insert():
    student_list = []
    while True:
        id = input("请输入Id：")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            english = int(input("英语："))
            python = int(input("python:"))
            math = int(input("math:"))
        except:
            print("请输入整数类型")
            continue
        # 将学生信息保存到字典
        student = {"id": id, "name": name, "english": english,
                   "python": python, "math": math
                   }
        # 将学生信息添加至列表
        student_list.append(student)
        answer = input("是否继续添加？y/n")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    # 保存
    save(student_list)
    print("学生信息录入完毕！！！")


def save(lst):
    try:
        stu_text = open(filename, "a", encoding="utf-8")
    except:
        # 如果没有文件，创建文件在写入
        stu_text = open(filename, "w", encoding="utf-8")
    for item in lst:
        stu_text.write(str(item) + "\n")
    stu_text.close()


def search():
    pass


def delete():
    while True:
        stu_id = input("请输入学生id:")
        if stu_id == "":
            break
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                student_list_old = file.readlines()
        else:
            student_list_old = []
        flag = False  # 标记是否删除
        # 判断列表是否为空
        if student_list_old:
            with open(filename, "w", encoding="utf-8") as w_file:
                d = {}
                for item in student_list_old:
                    # 将字符串转换成字典
                    d = dict(eval(item))
                    if d["id"] != stu_id:
                        w_file.write(str(d) + "\n")
                    else:
                        # 标记已删除
                        flag = True
                if flag:
                    print("%s的信息已删除" % stu_id)
                else:
                    print("没有找到ID为%s的学生" % stu_id)
        else:
            print("无学生信息")
            break
        # show()
        answer = input("是否继续删除？y/n")
        if answer == "n" or answer == "N":
            break


if __name__ == '__main__':
    while True:
        menu()
        choice = int(input("请选择："))
        if choice in range(0, 8):
            if choice == 0:
                answer = input("您确定要退出系统吗？y/n")
                if answer == 'y' or answer == 'Y':
                    print("谢谢使用")
                    break
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 7:
                show()
            elif choice == 0:
                exit()
