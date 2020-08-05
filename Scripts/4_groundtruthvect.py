import numpy as np
from tifffile import imsave, imread
from time import time
from progressbar import update_progress
import argparse

parser=argparse.ArgumentParser(
    description='''Filter on class 0 and formalizing class 1''')
parser.add_argument('-g','--groundtruth', help='Groundtruth image', required=True)
parser.add_argument('-p','--parcels', help='Parcel image', required=True)
args=parser.parse_args()


GRT = imread(args.groundtruth)
im_parcels = imread(args.parcels)


update_progress(0)
N = np.max(im_parcels)
GRT_vect = np.array([])
for n in range(1, N + 1):
    t_start = time()
    GRT_vect = np.append(GRT_vect, np.min(GRT[im_parcels == n]))
    update_progress((n-1)/(N-0.9), (time()-t_start)*(N-n-1))

update_progress(1)
    
np.save('/'.join(args.groundtruth.split('/')[:-1]) + '/grt.npy', GRT_vect.astype('uint8'))
