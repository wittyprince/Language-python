import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)  # 在0到10之间生成100个均匀分布的点作为x轴坐标
y_cbrt = np.cbrt(x)  # 计算每个x坐标对应的立方根值作为y轴坐标

fig, ax = plt.subplots()

color = 'tab:blue'
ax.plot(x, y_cbrt, label='cbrt(x)', color=color)  # 添加立方根函数曲线
ax.set_xlabel('x')  # 设置x轴标签
ax.set_ylabel('y', color=color)  # 设置y轴标签
ax.tick_params(axis='y', labelcolor=color)

# 显示完整的 x, -x, y, -y 轴
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

ax.spines['left'].set_linestyle('--')
ax.spines['bottom'].set_linestyle('--')

ax.spines['left'].set_bounds(-np.max(y_cbrt), np.max(y_cbrt))
ax.spines['bottom'].set_bounds(-np.max(x), np.max(x))

# 添加 -x, -y 轴标签
ax.text(-0.07, np.max(y_cbrt), '-y', color=color)
ax.text(np.max(x), -0.5, '-x', color=color)

# 添加 x, y 轴标签
ax.text(np.max(x)+0.2, 0.3, 'y', color=color)
ax.text(0.3, np.max(y_cbrt)+0.2, 'x', color=color)

ax.legend(loc='upper right')

plt.title('Cube Root Function')  # 设置图表标题
plt.grid(True)  # 显示网格线
plt.show()  # 显示图表