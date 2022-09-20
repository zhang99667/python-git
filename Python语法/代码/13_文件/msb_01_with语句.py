"""
with语句可以自动管理上下文资源，不论什么原因跳出with块
能确保文件正确地关闭，以此来达到释放资源的目的
"""
with open("./README.md","rb") as file:
    print(file)

