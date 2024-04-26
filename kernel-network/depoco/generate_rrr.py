import numpy as np
import cv2

def calculate_rotation_translation_error(R1, t1, R2, t2):
    R_rel = np.dot(R2, R1.transpose())  # 计算相对旋转矩阵
    r_rel, _ = cv2.Rodrigues(R_rel)  # 计算旋转矩阵的旋转向量表示
    t_err = t2 - np.dot(R_rel, t1)  # 计算平移向量的平移误差
    rotation_error = np.linalg.norm(r_rel)  # 计算旋转误差
    rotation_error_degrees = rotation_error * (180 / np.pi)  # 换算角度
    translation_error = np.linalg.norm(t_err)  # 计算平移误差
    return rotation_error_degrees, translation_error

# 定义旋转矩阵和平移向量
R1 = np.array([[-2.399388826807608011e-01, 9.707391968838517959e-01, 9.733663811875462729e-03],
               [-9.707727494748515928e-01, -2.399792468136777712e-01, 3.198433331682990627e-03],
               [5.440721913995913601e-03, -8.681747061185287814e-03, 9.999475115289904181e-01]])
t1 = np.array([5.864331909400000004e+05, 4.139159755921999924e+06, -2.110194200000000109e+01])
R2 = np.array([[-2.394453452282673811e-01, 9.708582081472346692e-01, 1.001330722871663845e-02],
               [-9.708939183212449420e-01, -2.394877550744105021e-01, 3.257995739584978838e-03],
               [5.561116374960511921e-03, -8.941747176025992283e-03, 9.999445580341463913e-01]])
t2 = np.array([5.864329703560000053e+05, 4.139158857607999817e+06, -2.109672399999999826e+01])

# 计算旋转误差和平移误差
rotation_error, translation_error = calculate_rotation_translation_error(R1, t1, R2, t2)

# 打印旋转误差和平移误差
print("Rotation Error: ", rotation_error)
print("Translation Error: ", translation_error)
