def Map(centers,data):
        center=[]
        datapoint=[]

        for dat in data:
            a=pool.apply_async(mapper, (centers,center,datapoint,dat ) ) 
        center, datapoint = a.get()

        d1=spark.createDataFrame(center)
        d1=d1.distinct().collect()
        return (center,datapoint,d1)
