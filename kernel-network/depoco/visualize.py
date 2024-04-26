import sys
sys.path.append('/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression')
import depoco.utils.point_cloud_utils as pcu
import argparse
import ruamel.yaml as yaml
from depoco.trainer import DepocoNetTrainer
import torch
import numpy as np
import open3d as o3d
if __name__ == "__main__":
    print('Hello')
    parser = argparse.ArgumentParser("./sample_net_trainer.py")
    parser.add_argument(
        '--config', '-cfg',
        type=str,
        required=False,
        default='config/kitti/e3.yaml',
        help='configitecture yaml cfg file. See /config/config for example',
    )
    parser.add_argument(
        '--number', '-n',
        type=int,
        default=29,
        help='Number of maps to visualize',
    )
    FLAGS, unparsed = parser.parse_known_args()

    print('passed flags')
    config = yaml.safe_load(open(FLAGS.config, 'r'))
    print('loaded yaml flags')
    trainer = DepocoNetTrainer(config)
    trainer.loadModel(best=False)
    print('initialized  trainer')
    a = trainer.submaps.getOrderedTrainSet()
    print()
    for i, batch in enumerate(trainer.submaps.getOrderedTrainSet()):
        #print(batch)
        with torch.no_grad():
            points_est,nr_emb_points,out = trainer.encode(batch)
            # print(f'batch是',{batch})
            print(
                f'nr embedding points: {nr_emb_points}, points out: {points_est.shape[0]}')
            pcu.visPointCloud(out['points'].detach().cpu().numpy())
            # me = torch.cat((out['points'],out['features']), dim=1)
            # np.save(f"/home/yy/campus_nudt/nudt_yy/nudt_run1_npy/reconstruction_{i}.npy", me.detach().cpu().numpy())
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(out['points'].detach().cpu().numpy())
            o3d.io.write_point_cloud(f"/home/yy/campus_nudt/nudt_yy/nudt_run0_npy/middle_{i}.pcd", pcd)
        if i+1 >= FLAGS.number:
            break
