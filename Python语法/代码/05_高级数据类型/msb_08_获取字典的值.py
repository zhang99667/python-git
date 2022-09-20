"""获取字典的元素"""

score = {"张三": 100, "王五": 98, "李四": 45}

"""第一种方式，使用[]"""
print(score["张三"])
print(score["王五"])

"""第二种方式，使用get()方法"""
print(score.get("张三"))
print(score.get("陈六"))  # None
print(score.get("嘛七", 99))  # 99是在查找 “嘛七” 所以应 value 不存在时候的默认值
