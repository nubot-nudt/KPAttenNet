import numpy as np
import open3d as o3d
import math
def matrix2quaternion(m):
    #m:array
    w = ((np.trace(m) + 1) ** 0.5) / 2
    x = (m[2][1] - m[1][2]) / (4 * w)
    y = (m[0][2] - m[2][0]) / (4 * w)
    z = (m[1][0] - m[0][1]) / (4 * w)
    return w,x,y,z


def rotation_translation(matrix):
    R = matrix[:3,:3]
    t = matrix[:3,3]
    return R, t

def compute_delat(R1,t1,R2,t2):
    dR = R2 @ np.linalg.inv(R1)
    dt = t2 - dR @ t1
    return dR,dt
def compute_tuple(a):
    w,x,y,z = a
    v= (x,y,z)
    v_norm = math.sqrt(x**2 +y**2 +z**2)
    log_a = (0,tuple(ai * math.atan2(v_norm,w)/v_norm for ai in v))
    return lo
def compute_ER(dR):
    
    quaterion = matrix2quaternion(dR)
    rotation_vector = np.asarray(quaterion.log())
    rotation_angle = np.linalg.norm(rotation_vector)
    return rotation_angle

M1 = np.asarray([[9.618568375123716097e-01, 2.732206420538668690e-01, -1.348721195694336898e-02, 5.863012808169999626e+05],
[-2.734872502697575092e-01, 9.593713633562936938e-01, -6.936361518672962134e-02, 4.138430884724999778e+06],
[-6.012326553487554529e-03, 7.040644805384271843e-02, 9.975002676700669424e-01, -1.637770899999999941e+01],
[0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.000000000000000000e+00]])
M2 = np.asarray([[9.618540299820594885e-01, 2.732303532726196305e-01, -1.349070264257554511e-02, 5.863012808090000181e+05],
[-2.734972214467489837e-01, 9.593689925605924929e-01, -6.935709029494654954e-02, 4.138430884717999958e+06],
[-6.007900480106998474e-03, 7.040106649613267487e-02, 9.975006741692097334e-01, -1.637770300000000034e+01],
[0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.000000000000000000e+00]])

R1,t1 = rotation_translation(M1)
R2,t2 = rotation_translation(M2)
dR, dt = compute_delat(R1,t1,R2,t2)
ER = compute_ER(dR)
print("E(R):",ER)
print("d(t):",dt)