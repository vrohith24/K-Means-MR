
def com(a,center,datapoint):
    count=0
    if dim == 3:
        sum1=[0,0,0]
    else:
        sum1=[0,0]
    
    for j in range(0,len(center)):
        if a == center[j]:
            count+=1
            sum1=add_dp(sum1,datapoint[j]);
    for k in range(0,dim):
        sum1[k] = sum1[k]/count;
    
    return sum1
def combine(d1,center,datapoint):
        new_centers=[]
        
        
        new_centers=[pool.apply(com, args=(a,center,datapoint))for a in d1]
        
        return new_centers
