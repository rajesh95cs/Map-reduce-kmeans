#!/bin/bash

#scaling the data
cat cleaned_space_data.csv | python3 Scaling_data.py > Scaled_space_data.txt

#changing permission
chmod +x Scaled_space_data.txt
#loading the scaled data to hdfs

hdfs dfs -copyFromLocal Scaled_space_data.txt /user/hduser/rajesh/kmeansin



#run the first mapreduce to get the initial centroids
mapred streaming -files  ./Mapperphase1.py,./Reducerphase1.py \
                 -mapper Mapperphase1.py \
                 -reducer Reducerphase1.py \
                 -input /user/hduser/rajesh/kmeansin \
                 -output /user/hduser/rajesh/kmeansphase1out

#get the centroids from hdfs
hdfs dfs -get /user/hduser/rajesh/kmeansphase1out/part-00000 initialcentroids.txt

#remove the outputdirectory in hdfs
hdfs dfs -rm -r /user/hduser/rajesh/kmeansphase1out

#change permissions
chmod +x initialcentroids.txt

#iteration begins
for (( i=1; i<=20; i++ ))
do      #second mapreduce
	mapred streaming -files ./initialcentroids.txt,./Mapperphase2.py,./Combinerphase2.py,./Reducerphase2.py \
                         -mapper Mapperphase2.py \
                         -combiner Combinerphase2.py \
                         -reducer Reducerphase2.py \
                         -input /user/hduser/rajesh/kmeansin \
                         -output /user/hduser/rajesh/kmeansphase2out
        #get the new centroids
        hdfs dfs -get /user/hduser/rajesh/kmeansphase2out/part-00000 newcentroids.txt
        #remove the phase2output in hdfs
        hdfs dfs -rm -r /user/hduser/rajesh/kmeansphase2out

        chmod +x newcentroids$i.txt
        #compare the number of lines in the new centroids and new one
        #if they are equal then our initial centroids will be replaced with the new one
	if [ "$(wc -l < newcentroids.txt)" -eq "$(wc -l < initialcentroids.txt)" ];
        then
            echo 'replace old centroids with new'
            cp newcentroids.txt initialcentroids.txt
            chmod +x initialcentroids.txt    
        fi
        rm -f newcentroids.txt
done

mv initialcentroids.txt finalcentroids.txt

chmod +x finalcentroids.txt
#mapreduce job 3

mapred streaming -files ./finalcentroids.txt,./Mapperphase3.py,./Reducerphase3.py \
                         -mapper Mapperphase3.py \
                         -reducer Reducerphase3.py \
                         -input /user/hduser/rajesh/kmeansin \
                         -output /user/hduser/rajesh/kmeansphase3out

#get the final cluster with key and points

hdfs dfs -get /user/hduser/rajesh/kmeansphase3out/part-00000 Finalcluster.txt

hdfs dfs -rm -r  /user/hduser/rajesh/kmeansphase3out

hdfs dfs -rm /user/hduser/rajesh/kmeansin/*


