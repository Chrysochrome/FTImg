import matplotlib.pyplot as plt
import numpy as np
import pylab
from PIL import Image
import warnings


class image:
    """
    图片处理类
    """

    def __init__(self, img):
        self.img = Image.open(img)
        self.aft_img = None
        self.test_img = None

    def getOrigPic(self):
        """
        返回原图片
        """
        return self.img

    def lConvert(self):
        """
        处理图像为灰度图像
        """
        self.aft_img = self.img.convert('L')
        return self.aft_img

    def testImg(self):
        """
        测试方法
        """
        self.test_img = Image.fromarray(self.matrixPic())

    def getdata(self):
        """
        获取图片信息
        e.g. (R, G, B) (L)

        return List
        """
        return self.aft_img.getdata()

    def histogram(self):
        """
        获取图片直方图
        """
        return self.aft_img.histogram()

    def size(self):
        """
        获取图片大小
        e.g. (255, 432)
        """
        return self.aft_img.size

    def height(self):
        """
        图片高度
        """
        return self.aft_img.size[1]

    def width(self):
        """
        图片宽度
        """
        return self.aft_img.size[0]

    def display(self, type='aft', name='pic'):
        """
        显示图片 (deprecated)
        """
        warnings.warn("display is deprecated. Use util instead.", DeprecationWarning, stacklevel=2)
        if type == 'ori' or self.aft_img == None:
            dis_img = self.img
        elif type == 'aft':
            dis_img = self.aft_img
        else:
            dis_img = None

        plt.figure(name)
        plt.imshow(dis_img)
        plt.axis('off')
        pylab.show()

    def matrixPic(self):
        """
        将图片处理为二维矩阵
        """
        pic_data = np.matrix(self.aft_img.getdata())
        matrix = np.reshape(
            pic_data, (self.aft_img.size[1], self.aft_img.size[0]))
        # width = self.aft_img.size[0]
        # for x in range(0, len(pic_data), width):
        #     row = pic_data[x:x + width]
        #     matrix.append(row)
        return matrix

    def matrixPicV(self):
        """
        将图片竖向处理为二维矩阵
        """
        matrix = self.matrixPic()
        matrixv = matrix.T
        return matrixv

    def testDisplay(self):
        """
        横排分割呈两张图片并排显示的效果

        (for test)
        """
        plt.subplot(1, 2, 1)
        plt.title('pic')
        plt.imshow(self.img)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title('L')
        plt.imshow(self.aft_img)
        plt.axis('off')
        pylab.show()
