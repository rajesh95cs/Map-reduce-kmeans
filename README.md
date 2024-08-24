K-means Clustering Using Hadoop MapReduce
This project implements the K-means clustering algorithm using Hadoop MapReduce. The code is structured into three phases that iteratively refine cluster centroids and assign data points to their respective clusters. The project is designed to handle large-scale data using a distributed computing approach.

Project Overview
Phase 1: Generates the initial centroids using MapReduce.
Phase 2: Iteratively updates the centroids based on the nearest data points. This phase includes a combiner for optimization.
Phase 3: Assigns data points to the final centroids and generates the final clusters.
How to Run the Project
Run the Bash Script: The entire process is automated using the kmeans.sh script.

bash
Copy code
bash kmeans.sh
View Results:

The final cluster assignment is saved as Finalcluster.txt in the working directory.
The final centroids can be viewed using:
bash
Copy code
more finalcentroids.txt
File Structure
kmeans.sh: Automates the entire process, including scaling data, running MapReduce jobs, and handling iterations.
Phase 1:
Mapperphase1.py
Reducerphase1.py
Phase 2:
Mapperphase2.py
Combinerphase2.py
Reducerphase2.py
Phase 3:
Mapperphase3.py
Reducerphase3.py
Scaling_data.py: Script to preprocess and scale the input data.
Notes
The script handles multiple iterations to refine centroids until convergence.
The code is optimized for large datasets using Hadoop’s distributed framework.
Requirements
Hadoop (MapReduce)
Python 3.x
Bash
