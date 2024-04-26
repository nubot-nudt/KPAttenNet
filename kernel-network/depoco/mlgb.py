import numpy as np

# 从二进制文件加载点云数据
points = np.fromfile("/home/yy/campus_nudt/nudt_yy/nudt_run1_bin/000022.bin", dtype=np.float32).reshape(-1, 3)

# 添加8个属性，将所有属性值初始化为0
new_attributes = np.zeros((points.shape[0], 8), dtype=np.float32)

# 将新属性连接到点云数据
points_with_attributes = np.concatenate((points, new_attributes), axis=1)

# 保存带有新属性的点云数据为新的二进制文件
points_with_attributes.astype(np.float32).tofile("/home/yy/campus_nudt/nudt_yy/nudt_run1_att/000022.bin")

print("New attributes added to point cloud data and saved as BIN file.")