def print_line(char, times):
    """打印单行分割线
    :param char: 分割线使用的分割字符
    :param times: 分割字符使用次数
    """

    print(char * times)


def print_lines(char, times, lines):
    """打印多行分割线

    :param char:分割线使用的分割字符
    :param times: 分割字符使用次数
    :param lines:分割线打印行数

    """

    i = 0
    while i < lines:
        print_line(char, times)
        i += 1

