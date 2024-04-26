import os
import numpy as np
import open3d as o3d

# 指定 PCD 文件夹路径和 BIN 文件夹路径
pcd_folder = "/home/yy/campus_nudt/raw/01"
bin_folder = "/home/yy/campus_nudt/campus_kitti/velodyne"
import os
import numpy as np
 
# 读取PCD文件并将其转换为numpy数组
def read_pcd(pcd_file):
    with open(pcd_file, 'r') as f:
        lines = f.readlines()
 
    data_start_idx = lines.index("DATA ascii\n") + 1
    point_cloud_data = [list(map(float, line.strip().split())) for line in lines[data_start_idx:]]
 
    return np.array(point_cloud_data, dtype=np.float32)
 
# 将点云数据保存为KITTI格式的BIN文件
def save_kitti_bin(point_cloud, bin_file):
    kitti_point_cloud = np.zeros((point_cloud.shape[0], 4), dtype=np.float32)
    kitti_point_cloud[:, :3] = point_cloud[:, :3]
    kitti_point_cloud[:, 3] = point_cloud[:, 3]
 
    kitti_point_cloud.tofile(bin_file)
 
# 指定输入PCD文件夹和输出KITTI格式BIN文件夹
pcd_folder = "/home/yy/campus_nudt/raw/01"      # 输入PCD文件夹
kitti_bin_folder = "/home/yy/campus_nudt/campus_kitti/velodyne"   # 输出KITTI格式BIN文件夹
 
# 确保输出文件夹存在
if not os.path.exists(kitti_bin_folder):
    os.makedirs(kitti_bin_folder)
 
# 遍历PCD文件夹中的所有文件并进行转换
for filename in os.listdir(pcd_folder):
    if filename.endswith('.pcd'):
        pcd_file = os.path.join(pcd_folder, filename)
        kitti_bin_file = os.path.join(kitti_bin_folder, os.path.splitext(filename)[0] + '.bin')
 
        point_cloud = read_pcd(pcd_file)
        save_kitti_bin(point_cloud, kitti_bin_file)
 
print("Conversion complete.")