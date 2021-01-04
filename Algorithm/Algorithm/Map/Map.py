def Map(centers,data):
        center=[]
        datapoint=[]
        for i in range(0,len(data)):
            a=mapper(centers,data[i])
            center.append(a[0])
            datapoint.append(a[1])
    
    
       # print(center,"center",len(center))
        d1=spark.createDataFrame(center)
        d1=d1.distinct().collect()
        #d1=d1.collect()
        #print(d1,'data Point',len(d1))
        return (center,datapoint,d1)


