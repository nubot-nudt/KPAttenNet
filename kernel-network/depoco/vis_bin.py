import open3d
import numpy as np

def read_display_bin_pc(path):
    points=np.fromfile(path,dtype=np.float32)
    points = np.reshape(points,(-1,11),order='F')
    
    print(f"points",points.shape)
    # .reshape(-1,3)
    points=points[:,:3]#open3d 只需xyz 与pcl不同
    print(points)
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
    opt.point_size=1.0
    # 添加点云
    vis.add_geometry(pcd)
    vis.run()

if __name__ == "__main__":
    bin = '/home/yy/campus_nudt/campus_kitti/01/velodyne/001453.bin'
    bin_normal = '/home/yy/campus_nudt/nudt_submap/01/000087.bin'
    bin_path = '/home/yy/Nuscene_submap/mini_val/000000.bin'
    read_display_bin_pc(bin_normal)