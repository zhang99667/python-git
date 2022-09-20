def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = {1, 2, 3}
gl_dict = {"name": "小明", "arg": 18}

# demo(gl_nums, gl_dict)  # ({1, 2, 3}, {'name': '小明', 'arg': 18})，字典会被当做元组
demo(*gl_nums, **gl_dict)

# 如果不使用拆包操作，需要将元组中的元素拆开
# demo(1, 2, 3, name="小明", age=18)
