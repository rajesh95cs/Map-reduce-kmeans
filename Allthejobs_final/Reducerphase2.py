#!/usr/bin/python3
#Reducer phase 2

from math import sqrt, floor
import os
import sys
import re
import numpy as np
from collections import defaultdict


if __name__== "__main__":
   points_sum = np.array([])
   rowcount = 0 
   data_row = []
   cent = defaultdict(list)
   data = []
   initial_key = -1
   current_key = -1
   totalcount = 0
   for line in sys.stdin:
      newlist = []
      r = [i for i in line.split(' ')]
      for i in r:
        x = re.sub("\[|\]|\{|\}|\:|,","",i)
        x = x.replace('\n','')
        #print(x)
        x = float(x)
        newlist.append(x)
      data.append(newlist)
   #print(centroids)
   for point in data:
     key = int(point[0])
     current_key = key
     value = point[1:-1]
     rowcount = int(point[-1])
     if current_key == initial_key:
        points_sum += value
        totalcount += rowcount
     else:
        if totalcount != 0:
           print(str(list(points_sum/rowcount)))
     
        initial_key = current_key
        points_sum = np.array(value)
        totalcount = rowcount
   if current_key == initial_key and totalcount != 0:
      print(str(list(points_sum/rowcount)))
  


