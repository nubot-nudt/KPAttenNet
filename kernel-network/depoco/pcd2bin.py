import os
import numpy as np

def read_pcd(filepath):
    lidar = []
    with open(filepath,'r',encoding='ISO-8859-1') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            if len(linestr) == 4:
                linestr_convert = list(map(float, linestr))
                lidar.append(linestr_convert)
            line = f.readline().strip()
    return np.array(lidar)



def convert(pcdfolder, binfolder):
    current_path = os.getcwd()
    ori_path = os.path.join(current_path, pcdfolder)
    file_list = os.listdir(ori_path)
    des_path = os.path.join(current_path, binfolder)
    if not os.path.exists(des_path):
        os.makedirs(des_path)
    for file in file_list: 
        (filename, extension) = os.path.splitext(file)
        velodyne_file = os.path.join(ori_path, filename) + '.pcd'
        pl = read_pcd(velodyne_file)
        pl = pl.reshape(-1, 4).astype(np.float32)
        
        # 调整形状为(-1, 11)
        pl_new = np.zeros((pl.shape[0], 11), dtype=np.float32)
        pl_new[:, :4] = pl
        
        # 添加7个新属性，赋值为零
        pl_new[:, 4:] = 0.0
        
        velodyne_file_new = os.path.join(des_path, filename) + '.bin'
        pl_new.tofile(velodyne_file_new)

if __name__ == "__main__":
    pcdfolder = '/home/yy/campus_nudt/nudt_yy/nudt_run0'
    binfolder = '/home/yy/campus_nudt/nudt_yy/nudt_run0_bin'
    convert(pcdfolder, binfolder)
