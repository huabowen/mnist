# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:12:13 2019

@author: Administrator
"""

from PIL import Image  
import numpy as np
im = Image.open("./MNIST_data/raw/mnist_train_0.jpg")
#im.show() 
img = np.array(im)      # image类 转 numpy
#img = img[:,:]
im=Image.fromarray(img) # numpy 转 image类
im.show() 