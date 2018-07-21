import numpy as np
from numpy import shape


class fft_basic:
    '''
    基础离散傅立叶变换类
    '''

    def __init__(self, matrix):
        self.matrix = matrix

    def do_fft(self):
        self.fft = np.fft.fft2(self.matrix)
        return np.log(np.abs(self.fft))

    def do_shift(self):
        self.fft_shift = np.fft.fftshift(self.fft)
        return np.log(np.abs(self.fft_shift))

    def get_fft(self):
        return self.fft
