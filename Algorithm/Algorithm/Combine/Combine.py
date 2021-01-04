def combine(d1,center,datapoint):
        new_centers=[]
        for i in range(0,len(d1)):
            count=0
            if dim == 3:
                sum1=[0,0,0]
            else:
                sum=[0,0]
            a = d1[i];
            for j in range(0,len(center)):
                if a == center[j]:
                    count+=1
                    sum1=add_dp(sum1,datapoint[j]);
            for k in range(0,dim):
                sum1[k] = sum1[k]/count;
            new_centers.append(sum1)
        if dim == 3:
            new_centers=spark.createDataFrame(new_centers,['X','Y','Z']).collect()
        else:
            new_centers=spark.createDataFrame(new_centers,['X','Y']).collect()
        #print(new_centers)
        return new_centers
