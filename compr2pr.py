import sys
sys.path.append('/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression')
#sys.path.append('/home/yy/deep-point-map-compression-fuxian/kppr')
import kppr
import kppr.models.models as models
import depoco.utils.point_cloud_utils as pcu
import argparse
import ruamel.yaml as yaml
from depoco.trainer import DepocoNetTrainer
import torch
import numpy as np

def pad(array, n_points=2000):
    """ array [n x m] -> [n_points x m]
    """
    if len(array.shape) == 2:
        out = np.zeros([n_points, array.shape[-1]], dtype='float32')
        mask = np.ones([n_points], dtype=bool)
        l = min(n_points, array.shape[-2])
        out[:l, :] = array[:l, :]
        mask[:l] = False
        return out, mask
    else:
        size = list(array.shape)
        size[-2] = n_points
        out = np.zeros(size, dtype='float32')
        mask = np.ones(size[:-1], dtype=bool)
        l = min(n_points, array.shape[-2])
        out[..., :l, :] = array[..., :l, :]
        mask[..., :l] = False
        return out, mask




if __name__ == "__main__":
    print('Hello')
    parser = argparse.ArgumentParser("./sample_net_trainer.py")
    parser.add_argument(
        '--config_compre', '-cfgcompre',
        type=str,
        required=False,
        default='/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression/depoco/config/compr2pr.yaml',
        help='configitecture yaml for compression cfg file. See /config/config for example',
    )
    parser.add_argument(
        '--config_pr', '-cfgpr',
        type=str,
        required=False,
        default='/home/yy/deep-point-map-compression-fuxian/kppr/kppr/config/config.yaml',
        help='configitecture yaml for place recognition cfg file. See /config/config for example',
    )

    parser.add_argument(
        '--number', '-n',
        type=int,
        default=1,
        help='Number of maps to visualize',
    )
    parser.add_argument(
        '--checkpoint','-ckpt',
        type=str,
        required=False,
        default='/home/yy/deep-point-map-compression-fuxian/kppr/kppr/experiments/kppr/lightning_logs/version_0/kppr.ckpt',
        help='checkpoint file for place recognition cfg file. See /config/config for example',
    )
    FLAGS, unparsed = parser.parse_known_args()
    model = models.KPPR.load_from_checkpoint(checkpoint_path=FLAGS.checkpoint).cuda()
    print(f"加载地点识别模型")
    
    model.eval()
    
    print('passed flags')
    config_compre = yaml.safe_load(open(FLAGS.config_compre, 'r'))
    print('loaded yaml flags')
    trainer = DepocoNetTrainer(config_compre)
    trainer.loadModel(best=False)
    print('initialized  trainer')

    a = trainer.submaps.getOrderedTrainSet()
    
    for i, batch in enumerate(trainer.submaps.getOrderedTrainSet()):
        #print(batch)
        bin_file = str(i)+'.bin'
        with torch.no_grad():
            #points_est,nr_emb_points = trainer.encodeDecode(batch)
            comprepoint,nr_emb_points,output_dict = trainer.encode(batch)
            #print(f'batch是',{batch})
            map = output_dict['map']
            is_in = np.isin(comprepoint.detach().cpu().numpy(),map.detach().cpu().numpy())
            print(
                f'nr embedding points: {nr_emb_points}, points out:')
            print(f"comprpoint的数据",{comprepoint.shape})
            print(f"map的数据",{map.shape})
            #comprepoint.detach().cpu().numpy().tofile(bin_file)
            #numpy.savetxt('a.txt',map,fmt='%0.8f')
            pcu.visPointCloud(comprepoint.detach().cpu().numpy())
            np.save(str(i)+'.npy',comprepoint.detach().cpu().numpy())
            input_reg = torch.cat((output_dict['points'],output_dict['features']),dim=1)
            print(input_reg.shape)
            input_reg,input_reg_maks = pad(input_reg.detach().cpu().numpy())
            input_reg = torch.tensor(input_reg).cuda()
            input_reg_maks = torch.tensor(input_reg_maks).cuda()
            input_reg = input_reg.unsqueeze(0).unsqueeze(0)
            input_reg_maks = input_reg_maks.unsqueeze(0).unsqueeze(0)
            derscrptor = model(input_reg,input_reg_maks)
            print(f"descriptor是",{derscrptor})
        if i+1 >= FLAGS.number:
            break
