#For finding euclidean distance
import math
#For spark session
from pyspark.sql import SparkSession

# to manipulate panadas data set
import numpy as np
import pandas as pd
#Pyspark modules
from pyspark.sql import Row
import pyspark
from pyspark.sql.types import StructType,StructField, DecimalType
import pyspark.sql.functions as f
from pyspark.sql.types import *
# To plot
from IPython.display import display
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits import mplot3d

# to find mean
from pyspark.sql.types import DecimalType
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import explode, col, udf, mean as _mean, stddev as _stddev


#Data Normalization
df1=datanormalization

dp=K_Means(df1.collect(),k,max_iter)
#to data frame
dc1=spark.createDataFrame(dp)
#to pandas Dataset
dc=dc1.toPandas().drop_duplicates()
dc1=dc1.toPandas()
dc=dc.values.tolist()
dc1=dc1.values.tolist()

#print(centers)

print(dc)

#collect the data and centre in dataset
data_n=[]
l=df1.collect()
if dim == 3:
    
    for i in range(0,len(dc)):
        a=dc[i]
        for j in range(0,len(l)):
            if a==dc1[j]:
                data_n.append([l[j][0],l[j][1],l[j][2],i+1])
        data_n.append([dc[i][0],dc[i][1],dc[i][2],i+1])
else :
    for i in range(0,len(dc)):
        a=dc[i]
        for j in range(0,len(l)):
            if a==dc1[j]:\
                data_n.append([l[j][0],l[j][1],i+1])
        data_n.append([dc[i][0],dc[i][1],i+1])
print(data_n)

#Genrate Data Frame
data_n=list(np.float_(data_n))

data_n=pd.DataFrame(data_n)


data_n
