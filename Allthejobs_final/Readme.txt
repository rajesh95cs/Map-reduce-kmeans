#to run the code 

#type bash kmeans.sh in the console

#results will be "Final cluster.txt" in the same directory

#for final centroids type : "more finalcentroids.txt" in the same directory

#notes:
#There are 3 phases in the code 
#phase1: generate initial centroids 
#phase2: generate the new centroids using previous centroids
#phase3: creating the cluster for final centroids
#each phase has got its own mapper and reducer except phase2 has got a combiner as well
