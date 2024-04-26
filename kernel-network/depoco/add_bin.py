import numpy as np

def add_properties_to_bin(input_file, output_file, num_properties=7):
    # 从二进制文件中读取点云数据
    point_cloud = np.fromfile(input_file, dtype=np.float32).reshape(-1, 4)

    # 确定新的点云维度和属性值
    num_points = point_cloud.shape[0]
    new_dim = 4 + num_properties
    new_properties = np.zeros((num_points, num_properties), dtype=np.float32)

    # 创建新的点云数组，包含旧的属性和新的属性
    new_point_cloud = np.concatenate((point_cloud, new_properties), axis=1)

    # 将新的点云保存为二进制文件
    new_point_cloud.astype(np.float32).tofile(output_file)

    print("Properties added to the point cloud.")

# 测试添加属性并保存的函数
add_properties_to_bin("/home/yy/campus_nudt/nudt_yy/nudt_run0_bin/small_pcd_0.bin", "/home/yy/campus_nudt/nudt_yy/nudt_run0_bin/small_pcd_output0.bin", 7)
