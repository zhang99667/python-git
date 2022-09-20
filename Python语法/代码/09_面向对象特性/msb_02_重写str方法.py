class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "我的名字是%s" % self.name


stu = Student("jack")
print(stu.__str__())
