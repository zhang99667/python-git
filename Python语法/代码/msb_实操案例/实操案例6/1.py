"""任务1：千年虫我来了"""

year = [82, 88, 89, 86, 85, 00, 99]
print("原列表:", year)

for index, value in enumerate(year):
    print(index, value)
    if str(value) != "0":
        year[index] = int("19" + str(value))
    else:
        year[index]=int("200"+str(value))
year.sort()
print("修改后的列表",year)