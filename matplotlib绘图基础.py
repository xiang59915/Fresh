from matplotlib import pyplot as plt

x = (2, 30, 2)
y = [11, 22, 33, 44, 11, 22, 33, 44, 8, 9, 55, 66, 44, 33, 88]
#设置图形大小
plt.figure(figuresize = (15, 15) dpi = 80)
# 绘图
plt.plot(x, y)
# 保存
plt.savefig("路径.png")
# 弹框
plt.show()
