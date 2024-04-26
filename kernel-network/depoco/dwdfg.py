import open3d as o3d
import numpy as np

# 从二进制文件加载点云数据
points = np.fromfile("/home/yy/output_with_attributes.bin", dtype=np.float32).reshape(-1, 11)
points = points[-1,:3]
# 创建Open3D点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# 可视化点云
o3d.visualization.draw_geometries([pcd])
