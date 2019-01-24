# FTImg

## 数字图像的傅立叶变换和余弦变换的实现

本项目为本科毕业设计，开源旨在供以后的同学们参考，从而顺利完成毕业设计。

基于[python3](https://www.python.org/downloads/ "下载python")，请使用相应版本的python运行。

## 构建依赖

    pip3 install matplotlib
    pip3 install Pillow
    pip3 install scipy

## 运行

    python3 main.py [your_pic_dir] <argv>

## 参数表

参数\<argv\> | 作用
-- | --
-f | FFT and display
-c | COS transfer and display
-g | Display gray image
-o | Display origin image
-of | Split to display origin and FFT image
-oc | Split to display origin and COS image
-ogf | Display orgin, gray and FFT image in same time
-ogc | Display orgin, gray and COS image in same time
-ogfc | Display orgin, gray, COS and FFT image in same time
-h --help | Display help info and exit
