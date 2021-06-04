#!usr/bin/python3
#scaling the data
import csv
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing
import re


for line in sys.stdin:
  data = [float(i) for i in line.split(",")]
  numpy_data = np.array(data)
  scaled_data_array = preprocessing.scale(numpy_data,with_std=True)
  scaled_data_list = list(scaled_data_array)
  scaled_data = ""
  for ele in scaled_data_list:
     if scaled_data_list.index(ele) == len(scaled_data_list)-1:
        scaled_data += str(ele)
        
     else:
        scaled_data += str(ele) + ","
  print(scaled_data)

