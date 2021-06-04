#!/usr/bin/python3
#mapper phase 3

from math import sqrt, floor
import csv
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing
from scipy.spatial import distance
import re

def mapper():
   centroids = []

   f = open('finalcentroids.txt','r')
   for cent in f:
     newlist = []
     r = [i for i in cent.split(',')]
     for i in r:
       x = re.sub("\[|\]|,","",i)
       x = x.replace('\n','')
       x = float(x)
       newlist.append(x)
     centroids.append(newlist)

   for line in sys.stdin:
     data = [float(i) for i in line.split(',')]
     distances = [distance.euclidean(data,center) for center in centroids]
     min_dist = min(distances)
     print(distances.index(min_dist),data)





if __name__ == "__main__":

   mapper()







