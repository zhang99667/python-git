score = {"张三": 100, "王五": 98, "李四": 45}

# 字典元素的遍历
# 取值的两种方式：1. score[中括号] 2. score.get() 方法
for item in score:
    print(item, score[item], score.get(item))
