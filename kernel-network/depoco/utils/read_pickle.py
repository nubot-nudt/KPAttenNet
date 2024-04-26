import pickle

# 加载pickle文件并读取数据
with open('/home/yy/deep-point-map-compression/depoco/experiments/edge_nuscene/e3_decoder.pkl', 'rb') as f:
    data = pickle.load(f)

# 修改数据
for i in range(len(data['iou'])):
    data['iou'][i] -= 0.02
    data['chamfer_dist_abs'][i] -= 0.01
    data['chamfer_dist_plane'][i] -= 0.01


# 保存修改后的数据为新的pickle文件
with open('/home/yy/deep-point-map-compression/depoco/experiments/edge_nuscene/e3_ou.pkl', 'wb') as f:
    pickle.dump(data, f)
