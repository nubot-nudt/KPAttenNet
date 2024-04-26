import os

# 指定点云文件所在的文件夹路径
folder_path = "/home/yy/campus_nudt/campus_kitti/velodyne"

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".bin"):
        # 构建原始文件路径
        old_file = os.path.join(folder_path, filename)
        
        # 构建目标文件路径，补全为6位
        new_file = os.path.join(folder_path, f"{int(filename.split('.')[0]):06d}.bin")
        
        # 对文件进行重命名
        os.rename(old_file, new_file)
        
        print(f"Renamed {old_file} to {new_file}")

print("File renaming complete!")
