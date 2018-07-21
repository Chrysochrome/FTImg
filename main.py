import getopt
import re
import sys
import time

# from tqdm import tqdm

from libs.image import image
from libs.img_intf import img_intf
from libs.util import util

print_str = '''Usage:
main.py [file ..] [arguments]\tOperate images

Arguments:
[Display Modes]:
-f\tFFT and display
-c\tCOS transfer and display
-g\tDisplay gray image
-o\tDisplay origin image
-of\tSplit to display origin and FFT image
-oc\tSplit to display origin and COS image
-ogf\tDisplay orgin, gray and FFT image in same time
-ogc\tDisplay orgin, gray and COS image in same time
-ogfc\tDisplay orgin, gray, COS and FFT image in same time

[Functions]:
-h --help\tDisplay this message
'''
# --save [path ..]\tSave choosed mode image

modules = {'FFT': False,
           'COS': False,
           'GRAY': False,
           'SAVE': False,
           'ORIG': False}


def display(argv):
    try:
        file = argv[0]
        # pattern = re.compile(r'(jpg|bmp|gif|ico|pcx|jpeg|tif|png|raw|tga)$')
        # if pattern.match(file) is None:
        #     print('Illegal file!')
        #     print('only jpg, bmp, gif, ico, pcx, jpeg, tif, png, raw, tga supported.')
        #     exit(1)
    except:
        print('[file ..] required!')
        print(print_str)
        exit(1)
    bool = True
    if '-f' in argv:
        bool = False
        modules['FFT'] = True
    if '-c' in argv:
        bool = False
        modules['COS'] = True
    if '-g' in argv:
        bool = False
        modules['GRAY'] = True
    if '-o' in argv:
        bool = False
        modules['ORIG'] = True
    if '-of' in argv:
        bool = False
        modules['FFT'] = True
        modules['ORIG'] = True
    if '-oc' in argv:
        bool = False
        modules['COS'] = True
        modules['ORIG'] = True
    if '-ogf' in argv:
        bool = False
        modules['FFT'] = True
        modules['GRAY'] = True
        modules['ORIG'] = True
    if '-ogc' in argv:
        bool = False
        modules['COS'] = True
        modules['GRAY'] = True
        modules['ORIG'] = True
    if '-ogfc' in argv:
        bool = False
        modules['COS'] = True
        modules['GRAY'] = True
        modules['FFT'] = True
        modules['ORIG'] = True
    if '-h' in argv or '--help' in argv:
        bool = False
        print(print_str)
        exit(0)
    if '--save' in argv:
        bool = False
        modules['SAVE'] = True

    if '--debug' in argv:
        bool = False
        print('File: %s' % file)
        print('Arguments: %s' % argv[1:])
        print(modules)
        # if '--raw' in argv:
        #     '''
        #     TODO: get raw
        #     '''
        #     cos_raw = None
        #     fft_raw = None
        #     print(cos_raw, fft_raw)

    if bool:
        print('Illegal argument!')
        print(print_str)
        exit(1)

    img = image(file)
    img_L = img.lConvert()
    utils = util()
    intf = img_intf(img.matrixPic())
    display_list = []
    start_t = time.time()
    if modules['ORIG'] == True:
        display_list.append(img.getOrigPic())
    if modules['GRAY'] == True:
        display_list.append(img_L)
    if modules['FFT'] == True:
        display_list.append(intf.fft_trans())
    if modules['COS'] == True:
        display_list.append(intf.cos_trans())
    print('Done, spend %ss' % str(round(time.time() - start_t, 2)))

    img_count = len(display_list)
    if img_count == 1:
        utils.display(display_list[0])
    elif img_count == 2:
        name = 'FFT'
        if modules['COS'] == True:
            name = 'COS'
        utils.display_split(display_list[0], display_list[1], name1_2=name)
    elif img_count == 3:
        name = 'FFT'
        if modules['COS'] == True:
            name = 'COS'
        utils.display_triple(
            display_list[0], display_list[1], display_list[2], name2_1=name)
    elif img_count == 4:
        utils.display_qua(
            display_list[0], display_list[1], display_list[2], display_list[3])
    else:
        print(print_str)
        exit()


display(sys.argv[1:])
