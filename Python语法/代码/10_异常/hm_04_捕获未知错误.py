try:
    # 提示用户输入一个数字
    num = int(input("请输入一个整数："))

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num

    print(result)

except ZeroDivisionError:
    print("被除数不能为 0 ")
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误！ %s" % result)
else:
    print("执行过程中无异常发生")
finally:
    print("无论是否出现异常都会执行")