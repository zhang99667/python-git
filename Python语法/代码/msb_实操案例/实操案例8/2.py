"""任务2：显示2019中超联赛前5名排行"""

scores = ({"广州恒大": 72}, {"北京国安": 70}, {"上海上港": 66}, {"江苏苏宁":53}, {"山东鲁能": 51})
for index, item in enumerate(scores):
    print(index + 1, end="\t")
    for keys in item:
        print(keys,item[keys])
