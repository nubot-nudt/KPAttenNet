import numpy as np

# 从二进制文件按照'C'顺序读取数据
data_c = np.fromfile("/home/yy/campus_nudt/nudt_yy/nudt_run1_att/000029.bin", dtype=np.float32)
points = data_c.reshape(-1, 11,order='C')
# 修改数据为'F'顺序
flattened_points = points.flatten(order='F') 


# 将数据保存为二进制文件
flattened_points.tofile("/home/yy/submaps/40m_ILEN/00/000029.bin")