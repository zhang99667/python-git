"""任务1：统计字符串中出现指定字符的次数"""


def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    s = "hellopythonhellojavahellogo"
    ch = input("请输入要统计的字符")
    print(get_count(s, ch))
