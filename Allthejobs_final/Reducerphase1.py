#! /usr/bin/python3
#reducer phase 1

import os,sys
import re

def reducer_cent():
   reducer_data = {}

   for line in sys.stdin:
       line_list = []
       outmap = [i for i in line.split(" ")]
       for out in outmap:
          x = re.sub("\[|\]|,","", out)
          x = x.replace('\n','')
          x = float(x)
          line_list.append(x)
       priority = line_list[0]
       point = line_list[1:-1]
       k = int(line_list[-1])
       if len(reducer_data) < k :
               reducer_data[priority] = point
       else :
            min_key = min(reducer_data.keys())
            if priority > min_key :
               del reducer_data[min_key]
               reducer_data[priority] = point

   for key in reducer_data.keys():
      print(reducer_data[key])

if __name__ == '__main__':
    reducer_cent()
