import numpy as np
import open3d
# data = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9],
#                 [10,11,12]])
# print(f"data的形状是{data.shape}")
# data_compre = np.array([[1,3,3],
#                 [1,2,3],
#                 [7,8,9],
#                 [10,11,12]])
# print(np.isin(data,data_compre))


def read_npy_bin_compa(path1,path2):
    points1=np.fromfile(path1,dtype=np.float64)
    points1 = points1.astype(np.float32)
    points1 = points1.reshape(-1,3)
    points1 = points1[:,:3]
    print(points1)
    points2 = np.load(path2)[:,0:3]
    print(points2)
    is_in = np.isin(points1.astype(np.float16),points2.astype((np.float16)))
    print(is_in)

def read_display_npy_pc(path):
    source_data = np.load(path)[:,0:3]  #10000x3
    print(source_data)
    print(source_data.shape)
    point_cloud = open3d.geometry.PointCloud()
    point_cloud.points = open3d.utility.Vector3dVector(source_data)
    open3d.visualization.draw_geometries([point_cloud])
if __name__ == "__main__":
    #lidar_path = r'/home/yy/oxford_compressed/oxford/2014-05-19-13-20-57/pointcloud_20m_10overlap/1400505893170765.npy'
    lidar_path1 = r'/home/yy/benchmark_datasets/oxford/2014-05-19-13-20-57/pointcloud_20m_10overlap/1400505893170765.bin'
    lidar_path2 = r'/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression/depoco/0.npy'
    #read_display_npy_pc(lidar_path)
    read_npy_bin_compa(lidar_path1,lidar_path2)
    print("end")