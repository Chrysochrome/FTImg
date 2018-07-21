import PIL

from libs.funcs.cos_basic import cos_basic
from libs.funcs.fft_basic import fft_basic


class img_intf:
    '''
    图像转换接口类，提供图片的转换输出方法
    '''

    def __init__(self, matrix):
        self.matrix = matrix

    def fft_trans(self):
        data = fft_basic(self.matrix)
        data.do_fft()
        return data.do_shift()

    def fft_trans_noshift(self):
        data = fft_basic(self.matrix)
        return data.do_fft()

    def fft_trans_raw(self):
        data = fft_basic(self.matrix)
        data.do_fft()
        return data.get_fft()

    def cos_trans(self):
        data = cos_basic(self.matrix)
        return data.do_cos()
