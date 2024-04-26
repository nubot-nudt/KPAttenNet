#coding=utf-8
import open3d as o3d
import numpy as np
np.set_printoptions(suppress=True) # 取消默认科学计数法，open3d无法读取科学计数法表示
data = np.load('/home/yy/apollo-compressed/TrainData/ColumbiaPark/2018-10-03/submaps/000046.npy')
b = np.array([1 , 1, 1,255, 255, 255]) # 每一列要除的数
np.savetxt('./scene.txt', data[:,:6]/b)
# 读取点云并可视化
pcd =o3d.io.read_point_cloud('./scene.txt', format='xyzrgb') # 原npy文件中的数据正好是按x y z r g b进行排列
print(pcd)
o3d.visualization.draw_geometries([pcd], width=1200, height=600)

