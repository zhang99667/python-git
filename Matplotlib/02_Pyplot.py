# 使用 plt 来引用 Pyplot 包的方法。
import matplotlib.pyplot as plt
import numpy as np

# 通过两个坐标 (0,0) 到 (6,100) 来绘制一条线:
x_points=np.array([0,6])
y_points=np.array([0,100])

# plot() 函数是绘制二维图形的最基本函数。
plt.plot(x_points,y_points)
plt.show()