import os
import numpy as np


def read_ori_pcd(input_path):
    lidar = []
    with open(input_path, 'r') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            if len(linestr) == 4:
                linestr_convert = list(map(float, linestr))
                lidar.append(linestr_convert)
            line = f.readline().strip()
    return np.array(lidar)


def read_labeled_pcd(filepath):
    lidar = []
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            if len(linestr) == 5:
                linestr_convert = list(map(float, linestr))
                lidar.append(linestr_convert)
            line = f.readline().strip()
    return np.array(lidar)


def convert2bin(input_pcd_dir, output_bin_dir):
    file_list = os.listdir(input_pcd_dir)
    if not os.path.exists(output_bin_dir):
        os.makedirs(output_bin_dir)
    for file in file_list:
        (filename, extension) = os.path.splitext(file)
        velodyne_file = os.path.join(input_pcd_dir, filename) + '.pcd'
        p_xyzi = read_ori_pcd(velodyne_file)
        p_xyzi = p_xyzi.reshape((-1, 4)).astype(np.float32)
        min_val = np.amin(p_xyzi[:, 3])
        max_val = np.amax(p_xyzi[:, 3])
        p_xyzi[:, 3] = (p_xyzi[:, 3] - min_val)/(max_val-min_val)
        p_xyzi[:, 3] = np.round(p_xyzi[:, 3], decimals=2)
        p_xyzi[:, 3] = np.minimum(p_xyzi[:, 3], 0.99)
        velodyne_file_new = os.path.join(output_bin_dir, filename) + '.bin'
        p_xyzi.tofile(velodyne_file_new)


def convert2label(input_pcd_dir, output_label_dir):
    file_list = os.listdir(input_pcd_dir)
    if not os.path.exists(output_label_dir):
        os.makedirs(output_label_dir)
    for file in file_list:
        (filename, extension) = os.path.splitext(file)
        velodyne_file = os.path.join(input_pcd_dir, filename) + '.pcd'
        p_xyz_label_object = read_labeled_pcd(velodyne_file)
        p_xyz_label_object = p_xyz_label_object.reshape((-1, 5))
        label = p_xyz_label_object[:, 3].astype(np.int32)
        label = label.reshape(-1)
        velodyne_file_new = os.path.join(output_label_dir, filename) + '.label'
        label.tofile(velodyne_file_new)


if __name__ == "__main__":
    ori_pcd_dir = "/home/yy/campus_nudt/nudt_yy/nudt_run_nopre"
    ori_bin_dir = "/home/yy/campus_nudt/nudt_yy/nudt_run0_bin"
    convert2bin(ori_pcd_dir, ori_bin_dir)

    # labeled_pcd_dir = "这里输入所有标注之后的点云pcd文件的存放目录"
    # labeled_bin_dir = "这里输入生成后的点云label文件的保存路径"
    # convert2label(labeled_pcd_dir, labeled_bin_dir)
