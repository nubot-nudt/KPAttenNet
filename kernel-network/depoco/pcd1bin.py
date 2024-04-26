import numpy as np
 
# 读取PCD文件
with open("/home/yy/campus_nudt/nudt_yy/nudt_run0/small_pcd_0.pcd", 'r',encoding='ISO-8859-1') as f:
    lines = f.readlines()
 
# 找到数据开始的行
data_start = 0
for i, line in enumerate(lines):
    if line.startswith("DATA binary\n"):
        data_start = i + 1
        break
 
# 解析点云数据
data = []
for i in range(data_start, len(lines)):
    values = lines[i].strip().split()
    if len(values) == 3:
        data.append([float(values[0]), float(values[1]), float(values[2])])
 
# 将点云数据转换为NumPy数组
point_cloud = np.array(data, dtype=np.float32)
 
# 将点云数据保存为BIN格式
point_cloud.tofile("/home/yy/campus_nudt/nudt_yy/nudt_run0_bin/small_pcd_0.bin")
 
print("PCD文件成功转换为BIN格式")