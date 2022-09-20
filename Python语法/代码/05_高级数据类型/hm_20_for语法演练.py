for num in range(1, 4):
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用 Break 退出了循环
    # 那么下方的else中的代码就不会被执行
    print("会执行吗？")
print("循环结束")
