import open3d
import numpy as np
def read_display_bin_pc(path):
    points=np.fromfile(path,dtype=np.float64)
    #print(f"points之前的形状是{points.shape}")
    points = points.reshape(-1,3)
    points=points[:,:3]#open3d 只需xyz 与pcl不同
    print(f"points的形状是{points.shape}")
    print(f"points是{points}")
    #将array格式的点云转换为open3d的点云格式,若直接用open3d打开的点云数据，则不用转换
    pcd=open3d.geometry.PointCloud()  # 传入3d点云格式
    pcd.points=open3d.utility.Vector3dVector(points)#转换格式
    # 设置颜色 只能是0 1 如[1,0,0]代表红色为既r
    pcd.paint_uniform_color([1,0,0])
    #创建窗口对象
    vis=open3d.visualization.Visualizer()
    # 创建窗口,设置窗口名称
    vis.create_window(window_name="point_cloud")
    # 设置点云渲染参数
    opt=vis.get_render_option()
    # 设置背景色（这里为白色）
    opt.background_color=np.array([255, 255, 255])
    # 设置渲染点的大小
    opt.point_size=2.0
    # 添加点云
    vis.add_geometry(pcd)
    vis.run()


def read_display_npy_pc(path):
    source_data = np.load(path)[:,0:3]  #10000x3
    print(source_data)
    print(source_data.shape)
    point_cloud = open3d.geometry.PointCloud()
    point_cloud.points = open3d.utility.Vector3dVector(source_data)
    open3d.visualization.draw_geometries([point_cloud])

def bin2npy_display_npy_pc(path):
    points=np.fromfile(path,dtype=np.float64)
    #print(f"points之前的形状是{points.shape}")
    points = points.reshape(-1,3)
    points=points[:,:3]
    print(points)
    print(points.shape)
    point_cloud = open3d.geometry.PointCloud()
    point_cloud.points = open3d.utility.Vector3dVector(points)
    open3d.visualization.draw_geometries([point_cloud])

if __name__ == "__main__":
    #lidar_path = r'/home/yy/oxford_compressed/oxford/2014-05-19-13-20-57/pointcloud_20m_10overlap/1400505893170765.npy'
    lidar_path = r'/home/yy/benchmark_datasets/oxford/2014-05-19-13-20-57/pointcloud_20m_10overlap/1400505893170765.bin'
    #read_display_npy_pc(lidar_path)
    bin2npy_display_npy_pc(lidar_path)
    #read_display_npy_pc(lidar_path)
    print("end")