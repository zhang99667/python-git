score = {"张三": 100, "王五": 98, "李四": 45}

# key 的判断
print("张三" in score)  # True
print("张三" not in score)  # False

# 删除指定的 key-value 对
del score["张三"]
# 清空字典
score.clear()
print(score)

# 新增 key-value 对
score["陈六"] = 98

# 修改 key-value 对
score["陈六"] = 100


