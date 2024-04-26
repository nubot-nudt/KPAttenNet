###此文件是根据submaps中的点云数据集进行的可视化调整，因为每个点云含有11个属性，而且排列方式和KITTI有所不用，所以按照高度给点云赋予了颜色,后面又按照label赋予颜色。
import numpy as np
import pcl
from pcl import pcl_visualization

lidar_path = r'/home/yy/campus_nudt/nudt_yy/nudt_run0/small_pcd_0.bin'
#lidar_path = r'/home/yy/campus_nudt/nudt_submap_normal/01/000051.bin'
points = np.fromfile(lidar_path,dtype = np.float64)
points = points.reshape(3,-1,order='C')
print(f"原始点云的形状是{points.shape}")
points=points.T
print(points[0:])
# points[:,3] = 65280
# points[20000:23000,3] = 3329330
# points[30000:34000,3] = 3329330
# points[50000:51000,3] = 3329330
# points[140000:148000,3] = 3329330
# points[points[:, 2] < 1, 3] = 65280
# points[23000:225000,3] = 13467442
# points = points[:,0:4]
print(points[23333,3])

color_cloud = pcl.PointCloud_PointXYZRGB(points)

visual = pcl.pcl_visualization.CloudViewing()
visual.ShowColorCloud(color_cloud,b'cloud')
flag = True
while flag:
    flag != visual.WasStopped()