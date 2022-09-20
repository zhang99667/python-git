def print_info(name,title="", gender=True):
    """
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    :rtype: object
    """
    gender_txt = "男生"
    if not gender:
        gender_txt = "女生"

    print(name, "是", gender_txt)


# 假设班上的同学，男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
# 多个缺省参数时，需要指明参数名称
print_info("小美", gender=False)
