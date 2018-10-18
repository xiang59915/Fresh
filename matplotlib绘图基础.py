from matplotlib import pyplot as plt
from matplotlib import font_manager

# 选用一个图表通用字体存为my_font，为显示中文
my_font = font_manager.FontProperties(fname="字体文件所在目录")

# 数据
x = range(11)
y = [1, 5, 6, 2, 11, 8, 9, 23, 5, 6, 8]

# 绘制折线图
plt.plot(x, y, label="图例名", color="折线颜色")
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

# 设置坐标
_xtick_label = ["{}年".format(i) for i in x]
plt.xticks(x, _xtick_label, fontproperties=my_font)

# 绘制网格
plt.grid(alpha= 0.4, linestyle="--")

# 展示
plt.show()
