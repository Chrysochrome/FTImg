import matplotlib.pyplot as plt
import pylab


class util:
    def __init__(self):
        pass

    def display(self, img, name='pic', name1_1='Result'):
        plt.figure(name)
        plt.imshow(img)
        plt.title(name1_1)
        plt.axis('off')
        pylab.show()

    def display_mat(self, mat, name='mat', name1_1='Matrix'):
        plt.figure(name)
        plt.imshow(mat, cmap='gray')
        plt.title(name1_1)
        plt.axis('on')
        pylab.show()

    def display_split(self, data1, data2, name='Summary', name1_1='Origin', name1_2='FFT'):
        plt.figure(name)
        plt.subplot(1, 2, 1)
        plt.title(name1_1)
        plt.imshow(data1)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title(name1_2)
        plt.imshow(data2)
        plt.axis('off')
        pylab.show()

    def display_triple(self, data1, data2, data3, name='Summary', name1_1='Origin', name1_2='Gray', name2_1='FFT'):
        plt.figure(name)
        plt.subplot(2, 2, 1)
        plt.title(name1_1)
        plt.imshow(data1)
        plt.axis('off')

        plt.subplot(2, 2, 2)
        plt.title(name1_2)
        plt.imshow(data2)
        plt.axis('off')

        plt.subplot(2, 2, 3)
        plt.title(name2_1)
        plt.imshow(data3)
        plt.axis('off')
        pylab.show()

    def display_qua(self, data1, data2, data3, data4, name='Summary', name1_1='Origin', name1_2='Gray', name2_1='FFT', name2_2='COS'):
        plt.figure(name)
        plt.subplot(2, 2, 1)
        plt.title(name1_1)
        plt.imshow(data1)
        plt.axis('off')

        plt.subplot(2, 2, 2)
        plt.title(name1_2)
        plt.imshow(data2)
        plt.axis('off')

        plt.subplot(2, 2, 3)
        plt.title(name2_1)
        plt.imshow(data3)
        plt.axis('off')

        plt.subplot(2, 2, 4)
        plt.title(name2_2)
        plt.imshow(data4)
        plt.axis('off')
        pylab.show()
