students = [
    {
        "name": "阿土",
        "age": 18,
        "gender": '男'
    },
    {
        "name": "小美",
        "age": 18,
        "gender": '女'
    },
    {
        "name": "李四",
        "age": 19,
        "gender": '男'
    }
]

find_name = input("输入要查找的姓名：")

for stu_dict in students:
    if stu_dict["name"] == find_name:
        print("查找成功", stu_dict)
        break
else:
    # 如果循环体内使用了 break 中断了循环，那么 for else 就不会被执行
    # 如果搜索所有字典检查之后，都没有发现搜索目标
    # 可以用 else 来进行一个统一的提示
    print("查找%s失败" % find_name)
