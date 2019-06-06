# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:57:35 2016

@author: cheng.zou
"""

import numpy as np

'''
ndarray : a multidimensional array object
'''
data_zeros = np.zeros((2,3))

data_1 = [2,6,3,8,1,15]
arr_1 = np.array(data_1)

data_2 = [[1,2,3],[4,5,6]]
arr_2 = np.array(data_2)
arr_2.ndim

data_3 = np.arange(0,15,0.5)
data_3.reshape(-1,3)

data = np.random.random((2,3))
data * 10
data + data
data.shape
data.dtype

