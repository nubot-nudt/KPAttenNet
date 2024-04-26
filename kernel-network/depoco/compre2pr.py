import sys
sys.path.append('/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression')

import depoco.utils.point_cloud_utils as pcu
import argparse
import ruamel.yaml as yaml
from depoco.trainer import DepocoNetTrainer
import torch
import numpy


if __name__ == "__main__":
    print('Hello')
    parser = argparse.ArgumentParser("./sample_net_trainer.py")
    parser.add_argument(
        '--config', '-cfg',
        type=str,
        required=False,
        default='config/compr2pr.yaml',
        help='configitecture yaml cfg file. See /config/config for example',
    )
    parser.add_argument(
        '--number', '-n',
        type=int,
        default=5,
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
    
    for i, batch in enumerate(trainer.submaps.getOrderedTrainSet()):
        #print(batch)
        bin_file = str(i)+'.bin'
        with torch.no_grad():
            #points_est,nr_emb_points = trainer.encodeDecode(batch)
            comprepoint,nr_emb_points,output_dict = trainer.encode(batch)
            #print(f'batch是',{batch})
            map = output_dict['map']
            is_in = numpy.isin(comprepoint.detach().cpu().numpy(),map.detach().cpu().numpy())
            print(
                f'nr embedding points: {nr_emb_points}, points out:')
            print(f"comprpoint的数据",{comprepoint.shape})
            print(f"map的数据",{map.shape})
            #comprepoint.detach().cpu().numpy().tofile(bin_file)
            #numpy.savetxt('a.txt',map,fmt='%0.8f')
            pcu.visPointCloud(comprepoint.detach().cpu().numpy())
            numpy.save(str(i)+'.npy',comprepoint.detach().cpu().numpy())

        if i+1 >= FLAGS.number:
            break
