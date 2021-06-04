#! /usr/bin/python3
# Mapper phase 1.py

from math import sqrt, floor
import csv
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing

def mapper(k):

  mappercent_dict = {}
  for line in sys.stdin: 
      point = [float(i) for i in line.split(',')]
      priority = np.random.uniform()
      if len(mappercent_dict) < k :
         mappercent_dict[priority] = point
      else :
         min_key = min(mappercent_dict.keys())
         if priority > min_key :
            del mappercent_dict[min_key]
            mappercent_dict[priority] = point
  
  for key in mappercent_dict:
     print(key,mappercent_dict[key],k)
       
  
if __name__ == "__main__":

  n_clusters=3

  mapper(n_clusters)
