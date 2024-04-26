import open3d as o3d
import numpy as np

#读取pcd数据并可视化
pcd_file=r"/home/yy/campus_nudt/nudt_yy/nudt_run1/small_pcd_22.pcd"
pcd=o3d.io.read_point_cloud(pcd_file,format='pcd')

#将点云的坐标和颜色转换为numpy格式
points=np.array(pcd.points)
colors=np.array(pcd.colors)
points.astype(np.float32).tofile("/home/yy/campus_nudt/nudt_yy/nudt_run1_bin/000022.bin")
#可视化
o3d.visualization.draw([pcd])
