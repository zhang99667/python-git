# *-* coding:utf-8 *-*
# coding = utf8

# 引号前面的 u 会告诉解释器，这是一个 utf8 编码格式的字符串
hello_str = u"你好"

print(hello_str)

for c in hello_str:
    print(c)
