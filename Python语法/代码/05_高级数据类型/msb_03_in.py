print("p" in "python")  # True
print("k" not in "python")  # True

lst = ["python", "hello", 10, 20]
print(10 in lst)  # True
print(100 in lst)  # False
print(100 not in lst)  # True


for item in lst:
    print(item)