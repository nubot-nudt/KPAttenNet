import numpy as np
import matplotlib.pyplot as plt

# 从txt文件读取点云数据
point_cloud_data = np.loadtxt('your_file.txt')

# 提取xy坐标
x = point_cloud_data[:, 0]
y = point_cloud_data[:, 1]

# 绘制xy坐标图
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('XY Coordinate Graph')
plt.grid(True)
plt.show()
