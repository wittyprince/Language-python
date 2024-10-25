import numpy as np
import matplotlib.pyplot as plt
import math

# 定义 x 的取值范围
x = np.linspace(-10, 10, 100)  # 在0到10之间生成100个均匀分布的点作为x轴坐标

# 指数函数：y = 2^x
y_exponential = 2 ** x

# 平方根
y_sqrt = np.sqrt(x) # 计算每个x坐标对应的平方根值作为y轴坐标
# 立方根
y_cbrt = np.cbrt(x)  # 计算每个x坐标对应的立方根值作为y轴坐标


# 绘制图形
# plt.plot(x, y_exponential, label='Exponential')
plt.plot(x, y_sqrt, label='sqrt')                       # 绘制平方根函数的曲线
plt.plot(x, -y_sqrt, label='-sqrt(x)')                  # 绘制负平方根函数的曲线
plt.plot(x, y_cbrt, label='cbrt(x)')                    # 绘制立方根函数的曲线
# plt.plot(x, y_logarithm, label='Logarithm')
# plt.plot(x, y_square, label='Square')
# plt.plot(x, y_cube, label='Cube')

plt.xlabel('x')             # 设置x轴标签
plt.ylabel('y')             # 设置y轴标签

plt.title('Root Function')  # 设置图表标题
plt.legend()                # 显示图例
plt.grid(True)              # 显示网格线

plt.show()                  # 显示图表



# 要绘制平方根函数的图像，您可以使用Python中的Matplotlib库。下面是一个简单的示例代码来绘制平方根函数的图像：

