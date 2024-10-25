import numpy as np
import matplotlib.pyplot as plt

# 定义 x 的取值范围
x = np.linspace(-10, 10, 100)

# 指数函数：y = 2^x
y_exponential = 2 ** x

# 对数函数：y = log₂(x)
y_logarithm = np.log2(x)

# 线性函数：y = 2x + 1
# y_linear = 2 * x + 1
y_linear = x

# 平方函数：y = x²
y_square = x**2

# 立方函数：y = x³
y_cube = x**3

# xlogx函数：y = xlog₂(x)
y_xlogx = x * np.log2(x)

# logx函数：y = log₂(x)
y_logx = np.log2(x)

# 绘制图形
# plt.plot(x, y_exponential, label='Exponential')
# plt.plot(x, y_logarithm, label='Logarithm')
plt.plot(x, y_linear, label='Linear')
# plt.plot(x, y_square, label='Square')
# plt.plot(x, y_cube, label='Cube')
plt.plot(x, y_xlogx, label='xlogx')
plt.plot(x, y_logx, label='logx')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.show()
