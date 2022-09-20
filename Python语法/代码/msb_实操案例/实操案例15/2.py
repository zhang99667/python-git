# 任务2：模拟淘宝客服自动回复
def find_answer(question):
    with open("replay.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            # 字符串分割
            keyword = line.split("|")[0]
            replay = line.split("|")[1]
            if keyword in question:
                return replay


if __name__ == '__main__':
    question = input("输入：")
    # 在文件中查找
    replay = find_answer(question)
    if not replay:  # 如果回复的是 False ，not False -> True
        question = input("请输入与关键字，订单、物流、账户、支付")
    else:
        print(replay)
