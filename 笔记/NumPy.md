# Nmpy 是什么？

#### Numpy (Numerical Pythonl 的缩写)：

- 一个 **开源** 的 Python **科学计算库**

- 使用 NumPy 可以方便的使用 **数组**、**炬阵** 进行计算
- 包含 **线性代数**、**傅里叶变换**、**随机数生成** 等大量函数

# 为什么使用 Numpy？

#### 对于同样的数值计算任务，使用 Numpy 比直接编写 Python 代码实现，优点：

- **代码更简洁**：Numpy 直接以 **数组**、**矩阵** 为 **粒度** 计算并且 **支持大量的数学函数**，而 Python 需要用 for 循环从底层实现；

- **性能更高效**：Numpy 的数组存储效率和输入输出计算性能，比 Python 使用 List 或者嵌套 List 好很多；
  - 注：Numpy 的数据存储和 Python 原生的 List 是 **不一样的**)
  - 注：Numpy 的 **大部分代码都是 C 语言实现的**，这是 Numpy 比纯 Python 代码高效的原因；

#### Numpy 是 Python 各种数据科学类库的基础库

- 比如 `SciPy`、`Scikit-Learn`、`Tensorflow`、`PaddlePaddle` 等
- 如果不会 Numpy ，这些库的深入理解都会遇到障碍

# 怎样安装 Numpy?

> 如果安装的是 Anaconda ，**则自带了 numpy :**

Anaconda 是 Python 最流行的一个已经集成了非常多类库的安装包

不论是学习、实验、线上部署 Anaconda 当前都是使用 Python 的首选安装环境

#### 如果安装的是官网的 Python，则可以用 pip 安装 Numpy

在命令行下使用 `pip install numpy` 即可安装

#### 验证是否安装了 Numpy，进入 Python 命令行

输入 `import numpy as np`，如果没报错则安装成功

# Numpy 与原生 Python 的性能对比

##### 需求：

- 实现两个数组的加法
- 数组 `A` 是 `1~N` 数字的平方
- 数组 `B` 是 `1~N` 数字的立方

##### 对比使用 Numpy 和原生 Python 的性能对比