import numpy as np
import sys
sys.path.append('/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression')
import matplotlib.pyplot as plt
import glob
import argparse
from ruamel import yaml
import depoco.utils.point_cloud_utils as pcu
plt.rcParams.update({'font.size': 20})
#plt.rcParams.update({'font.size': 16})
def plotResults(files, x_key, y_key, ax, draw_line=False, label=None, set_lim=True):
    x = []
    y = []
    for f in files:
        eval_dict = pcu.load_obj(f)
        if((x_key in eval_dict.keys()) & (y_key in eval_dict.keys())):
            for v in eval_dict.values():
                v = np.array(v)
            if not draw_line:
                ax.plot(np.mean(eval_dict[x_key]),
                        np.mean(eval_dict[y_key]), '.')
                ax.text(np.mean(eval_dict[x_key]), np.mean(
                    eval_dict[y_key]), f.split('/')[-1][:-4])

            x.append(np.mean(eval_dict[x_key]))
            y.append(np.mean(eval_dict[y_key]))
    print(f"{label}的x是{x}")
    print(f"{label}的y是{y}")
    if draw_line:
        line, = ax.plot(x, y, '-x', label=label,linewidth=3,markersize=8)
        # line.set_label(label)

    ax.set_xlabel(x_key,fontsize=24)
    ax.set_ylabel(y_key,fontsize=24)

    if set_lim:
        ax.set_xlim(0,None)
        ax.set_ylim(0,None)
    # ax.grid()


def genPlots(files, f, ax, draw_line=False, label=None, x_key='memory'):
    # print('shape',ax[0,0])
    plotResults(files, x_key=x_key, y_key='chamfer_dist_abs',
                ax=ax[0], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='chamfer_dist_plane',
    #             ax=ax[0], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='iou',
    #             ax=ax[0], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='reconstruction_error',
    #             ax=ax[3], draw_line=draw_line, label=label)


if __name__ == "__main__":
    ####### radius fct ##############
    path = 'experiments/results/kitti/'
    files = sorted(glob.glob(path+'*.pkl'))
    path_raw = 'experiments/kitti_raw/'
    files_raw = sorted(glob.glob(path_raw+'*.pkl'))
    path_oa = 'experiments/kitti_3atte/'
    files_oa = sorted(glob.glob(path_oa+'*.pkl'))
    path_atte = 'experiments/kitti_atte/'
    files_atte = sorted(glob.glob(path_atte+'*.pkl'))
    path_deco = 'experiments/kitti_deco/'
    files_deco = sorted(glob.glob(path_deco+'*.pkl'))
    path_edge = '/home/yy/deep-point-map-compression/depoco/experiments/edgemodel/'
    files_edge = sorted(glob.glob(path_edge+'*.pkl'))
    f, ax = plt.subplots(1, 2)
    f.suptitle('Radius FPS')
    genPlots(files, f, ax, draw_line=True, label='Depoco', x_key='bpp')
    #genPlots(files_oa, f, ax, draw_line=True, label='ours_en', x_key='bpp')
    genPlots(files_deco, f, ax, draw_line=True, label='Ours_KPConv', x_key='bpp')
    genPlots(files_edge, f, ax, draw_line=True, label='Ours_EDGEConv', x_key='bpp')
    
    ax[0].axhline(y=0,linewidth=5,color='black')
    ax[0].axvline(x=0,linewidth=5,color='black')
    for a in ax:
        a.grid()
        a.set_ylim([0,0.15])
        a.legend()
    plt.show()
