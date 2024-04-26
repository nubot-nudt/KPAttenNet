import open3d as o3d
import numpy as np
import math
# 指定PCD文件路径

def load_pcd_to_ndarray(pcd_path):
    with open(pcd_path) as f:
        while True:
            ln = f.readline().strip()
            if ln.startswith('DATA'):
                break

        points = np.loadtxt(f)
        print(points.shape)
        # points = points[:, 0:4]
        xyz = points[:, 0:3]
        rpy = points[:, 4:7]
        print(f"xyz是",xyz)
        print(f"rpy是",rpy)
        trans = np.concatenate([xyz,rpy],axis=1)
        return points


def eulerAnglesToRotationMatrix(theta) :
    
    R_x = np.array([[1,         0,                  0                   ],
                        [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                        [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                        ])
            
            
                        
    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                        [0,                     1,      0                   ],
                        [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                        ])
                    
    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                        [math.sin(theta[2]),    math.cos(theta[2]),     0],
                        [0,                     0,                      1]
                        ])
                        
                        
    R = np.dot(R_z, np.dot( R_y, R_x ))

    return R

def odometry_to_positions(odometry):
    rot = eulerAnglesToRotationMatrix(odometry[3:])
    t = odometry[:3].reshape(3,1)
    odometry = np.hstack((rot, t))    
        # T_w_cam0 = odometry.reshape(3, 4)
    T_w_cam0 = np.vstack((odometry, [0, 0, 0, 1]))
    return T_w_cam0

pcd_path = "/home/yy/campus_nudt/pose/01/transformations.pcd"
points = load_pcd_to_ndarray(pcd_path)
points_xyzrpy = points[:,:6]
print(points_xyzrpy)
output_file = open("/home/yy/campus_nudt/campus_kitti/01/poses.txt", "w")
for row in points_xyzrpy:
    matrix = odometry_to_positions(row)
    np.savetxt(output_file, matrix.reshape(1, -1), delimiter=" ", fmt="%.12f")
    # for row in matrix:
    #     output_file.write(" ".join(str(value) for value in row) + "\n")
# array = np.random.random(6)
# juzhen = odometry_to_positions(array)
output_file.close()

# # 加载PCD文件
# pcd = o3d.io.read_point_cloud(pcd_path)
# # print(pcd.shape)
# # 获取点云数据
# xyz2 = np.asarray(pcd.points)
# colors = np.asarray(pcd.normals)

# # 打印点云数据
# print(xyz2.shape)
# print(xyz2)
# print(colors)
