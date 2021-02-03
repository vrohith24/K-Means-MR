#Get Centers
centers=rdd.map(lambda x:ad(x)).collect()
centers=spark.createDataFrame(centers,['X', 'Y','Z']).collect()
centers

def Find_dist(x,y):
    sum = 0
    vec1= list(x)
    vec2 = list(y)
    for i in range(len(vec1)):
        sum = sum +(vec1[i]-vec2[i])*(vec1[i]-vec2[i])
    sum=math.sqrt(sum)
    return sum
#Mapper
def rt(n,y):
    sum=10000000
    for i in y:
        j=Find_dist(n,i)
        if j<sum:
            sum=j
            k=i
        
    return (k,n)
rdd = sc.parallelize(exdt.collect())
y=centers
rdd2 = rdd. map (lambda x : (rt(x,y)))
exdt.show()
rdd2

#Combine

def to_list(a):
    return [a]

def add_to_end(a, b):
    a.append(b)
    return a

def Merge(a, b):
    a.extend(b)
    return a
def Combine(KV):
    return sorted(KV.combineByKey(to_list, add_to_end, Merge).collect())

#Algorithm
def K_Means(data,k,max_iter):
    exdt=spark.createDataFrame(data)
    exd=exdt.distinct()
    centers =exd.rdd.takeSample(False,k,seed=49)
    print(centers)
    for i in range(0,max_iter):
        
        rdd = sc.parallelize(exdt.collect())
        Key_Value_rdd= rdd.map (lambda x : (rt(x,centers)))
        
        KV_list=Combine(Key_Value_rdd)
        #REDUCE
        KV_list=spark.createDataFrame(KV_list).select("_2")
        rdd = sc.parallelize(KV_list.collect())
        centers=rdd.map(lambda x:ad(x)).collect()
        
    return Key_Value_rdd.collect()
#Data set
l=[(1,2,1),(2,3,3),(2,2,1),(4,2,3),(3,5,3),(0,3,1),(2,1,4)]
exdt1=spark.createDataFrame(l, ['X', 'Y',"Z"])
exdt1 = exdt1.withColumn("X",exdt1["X"].cast(DecimalType()))
exdt1 = exdt1.withColumn("Y",exdt1["Y"].cast(DecimalType()))
exdt1 = exdt1.withColumn("Z",exdt1["Z"].cast(DecimalType()))
(mno)=K_Means(exdt1.collect(),3,10)


mno=spark.createDataFrame(mno)
mno.show()
c=mno.select("_1").distinct().collect()
c2=mno.collect()
