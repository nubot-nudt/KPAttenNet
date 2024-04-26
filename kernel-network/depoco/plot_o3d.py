import open3d
import numpy as np
def read_display_bin_pc(path):
    ###先调整为float32
    #points=np.fromfile(path,dtype=np.float64)
    points=np.fromfile(path,dtype=np.float64)
    #print(f"points之前的形状是{points.shape}")
    points = points.reshape(-1,11)
    points=points[:,:3]#open3d 只需xyz 与pcl不同
    print(f"points的形状是{points.shape}")
    print(f"points是{points}")
    np.savetxt('b.txt',points,fmt='%0.8f')
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



def read_display_bin_pc2(path):
    ###先调整为float32
    #points=np.fromfile(path,dtype=np.float64)
    points=np.fromfile(path,dtype=np.float32)
    #print(f"points之前的形状是{points.shape}")
    points = points.reshape(-1,11)
    points=points[:,:3]#open3d 只需xyz 与pcl不同
    print(f"points的形状是{points.shape}")
    print(f"points是{points}")
    np.savetxt('b.txt',points,fmt='%0.8f')
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

if __name__ == "__main__":
    lidar_path = r'/home/yy/submaps/40m_ILEN/00/000000.bin'
    #lidar_path = r'/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression/depoco/0.npy'
    #read_display_npy_pc(lidar_path)
    read_display_bin_pc(lidar_path)
    print("end")