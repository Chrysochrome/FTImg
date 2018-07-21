import numpy as np
from numpy import shape
from scipy import fftpack


class cos_basic:
    '''
    基础离散余弦变换类
    '''

    def __init__(self, matrix):
        self.matrix = matrix

    def do_cos(self):
        data =  fftpack.dct(fftpack.dct(self.matrix, axis=0, norm='ortho'), axis=1, norm='ortho')
        return np.log(np.abs(data))
