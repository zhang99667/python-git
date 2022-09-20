##### array 对象的背景：

- `Numpy` 的 **核心数据结构**，就叫做 `array` 就是 **数组**，`array` 对象可以是 **一维数组**，**也可以是多维数组**；
- `Python` 的 `List` 也可以实现相同的功能，但是 `array` 比 `List` 的优点在于 **性能好**、**包含数组元数据信息**、**大量的便捷函数**；
- `Numpy` 成为事实上的 `Scipy`、`Pandas`、`Scikit-Learn`、`Tensorflow`、`PaddlePaddle` 等框架的 **“通用底层语言”**
- `Numpy` 的 `array` 和 `Python` 的 `List` 的一个区别，是它 **元素必须都是同一种数据类型**，比如都是数字 `int` 类型，这也是 `Numpy` 高性能的一个原因；

##### array 本身的属性

- `shape` : 返回一个元组，表示 `array` 的维度
- `ndim` : 一个数字，表示 `array` 的维度的数目
- `size` : 一个数字，表示 `array` 中所有数据元素的数目
- `dtype` : `array` 中元素的数据类型

##### 创建 array 的方法

- 从 `Python` 的列表 `List` 和嵌套列表创建 `array`
- 使用预定函数 `arange`、`ones/ones_like`【**数组全为 1**】、`zeros/zeros_like`【**数组全为 0**】、`empty/empty_like`【**数组全为空**】、`full/full_like`【**数组全为指定数值**】、`eye`【**矩阵对角线全为 1**】 等函数创建
- **生成随机数** 的 `np.random` 模块构建

##### `array` 本身支持的大量操作和函数

- 直接 **逐元素的加减乘除** 等算数操作


- 更好用的 **面向多维的数组索引**

- 求 `sum/mean` 等 **聚合函数**
- 线性代数函数，比如 **求解逆矩阵**、**求解方程组**