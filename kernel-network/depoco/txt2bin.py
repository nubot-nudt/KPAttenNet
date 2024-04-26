import numpy as np

def convert_txt_to_bin(txt_file, bin_file):
    # 从文本文件中读取点云数据
    point_cloud = np.loadtxt(txt_file)

    # 保存点云数据为二进制文件
    point_cloud.astype(np.float32).tofile(bin_file)

    print("TXT to BIN conversion complete.")

# 测试转换函数
convert_txt_to_bin("/home/yy/campus_nudt/nudt_yy/nudt_run0/small_pcd_0.txt", "/home/yy/campus_nudt/nudt_yy/nudt_run0/small_pcd_0.bin")
