import open3d as o3d
import numpy as np

# 从二进制文件加载点云数据
data = np.fromfile("/home/yy/apollo/000020.bin", dtype=np.float32)  # 根据您的点云数据格式相应修改dtype和文件路径
points = data.reshape(-1, 4,order='C')
print(points.shape)
points = points[:,:3]
# 创建Open3D点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.asarray(points))

# 可视化点云
o3d.visualization.draw_geometries([pcd])
