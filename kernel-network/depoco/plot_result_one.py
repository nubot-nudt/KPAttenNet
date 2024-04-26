import numpy as np
import sys
sys.path.append('/home/yy/deep-point-map-compression-fuxian/deep-point-map-compression')
import matplotlib.pyplot as plt
import glob
import argparse
from ruamel import yaml
import depoco.utils.point_cloud_utils as pcu
plt.rcParams.update({'font.size': 16})
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
    print(f"x是{x}")
    print(f"y是{y}")
    if draw_line:
        line, = ax.plot(x, y, '-x',linewidth=2, label=label)
        # line.set_label(label)

    ax.set_xlabel(x_key)
    ax.set_ylabel(y_key)

    if set_lim:
        ax.set_xlim(0,None)
        ax.set_ylim(0,None)
    # ax.grid()


def genPlots(files, f, ax, draw_line=False, label=None, x_key='memory'):
    # print('shape',ax[0,0])
    plotResults(files, x_key=x_key, y_key='chamfer_dist_abs',
                ax=ax[0], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='chamfer_dist_plane',
    #             ax=ax[1], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='iou',
    #             ax=ax[2], draw_line=draw_line, label=label)
    # plotResults(files, x_key=x_key, y_key='reconstruction_error',
    #             ax=ax[0], draw_line=draw_line, label=label)


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
    f, ax = plt.subplots(1, 2)
    f.suptitle('Radius FPS')
    genPlots(files, f, ax, draw_line=True, label='depo', x_key='bpp')
    genPlots(files_oa, f, ax, draw_line=True, label='ours_en', x_key='bpp')
    genPlots(files_deco, f, ax, draw_line=True, label='ours_de', x_key='bpp')
    #genPlots(files_extra, f, ax, draw_line=True, label='extra', x_key='bpp')
    # draco_line_x = [0.10,0.26,0.67]
    # draco_line_y = [0.41,0.22,0.12]
    octree_line_x = [0.08,0.26,0.56]
    octree_line_y = [0.23,0.12,0.09]
    # mpeg_line_x_de = [0.1,0.12,0.35,0.75]
    # mpeg_line_y_de = [0.41,0.25,0.12,0.11]
    # mpeg_line_x_dt = [0.1,0.12,0.35,0.75]
    # mpeg_line_y_dt = [0.23,0.116,0.054,0.046]
    # mpeg_line_x_iou = [0.1,0.12,0.35,0.75]
    # mpeg_line_y_iou = [0.01,0.04,0.18,0.33]
    # mpeg_line_x_re = [0.1,0.12,0.35,0.75]
    # mpeg_line_y_re = [0.16,0.092,0.043,0.032]
    # ax[0].plot(draco_line_x,draco_line_y, color='red',marker='x', label='draco')
    ax[0].plot(octree_line_x,octree_line_y, color='red',marker='x', label='octree')
    # ax[0].plot(mpeg_line_x_de,mpeg_line_y_de, color='green',marker='x', label='mpeg')
    # ax[1].plot(mpeg_line_x_dt,mpeg_line_y_dt, color='green',marker='x', label='mpeg')
    # ax[2].plot(mpeg_line_x_iou,mpeg_line_y_iou, color='green',marker='x', label='mpeg')
    # ax[3].plot(mpeg_line_x_re,mpeg_line_y_re, color='green',marker='x', label='mpeg')
    for a in ax:
        a.grid()
        a.set_ylim([0,0.2])
        a.legend()
    plt.show()
