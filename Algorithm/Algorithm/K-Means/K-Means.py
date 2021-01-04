def K_Means (data,k,max_iter):
#generate centers
    exdt=spark.createDataFrame(data)
    exd=exdt.distinct()
    centers = exd.rdd.takeSample(False,k,seed=49)
    
    
    
    # MAP
    for m in range (0,max_iter) :
        (center,datapoint,d1)=Map(centers,data)
                
    #COMBINE
        new_centers=combine(d1,center,datapoint)
        
        #print(new_centers)
    #REDUCE
        (centers)=Reduce(d1,center,new_centers)
        
       
    
    return center
