"""任务2：定义学生类录入5个学生信息存储到列表中"""


class Student(object):
    def __init__(self, stu_name, stu_age, stu_gender, stu_score):
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_gender = stu_gender
        self.stu_score = stu_score

    def __str__(self):
        print(self.stu_name, self.stu_age, self.stu_gender, self.stu_score)


if __name__ == '__main__':
    print("请输入：姓名#年龄#性别#成绩")
    lst = []
    for i in range(0, 5):
        s = input("输入%d位学生信息" % (i + 1))
        s_lst = s.split("#")  # 以'#'号进行分割
        # 创建学生对象
        stu = Student(s_lst[0], int(s_lst[1]), s_lst[2], float(s_lst[3]))
        lst.append(stu)

    for item in lst:
        item.__str__()