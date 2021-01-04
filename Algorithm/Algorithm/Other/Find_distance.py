def Find_dist(x,y):
    sum = 0
    if dim == 3:
        
        sum+=(x[0]-y[0])*(x[0]-y[0])
        sum+=(x[1]-y[1])*(x[1]-y[1])
        sum+=(x[2]-y[2])*(x[2]-y[2])
    else:
        sum+=(x[0]-y[0])*(x[0]-y[0])
        sum+=(x[1]-y[1])*(x[1]-y[1])
        
   # for i in range(len(vec1)):
    #    sum = sum +(vec1[i]-vec2[i])*(vec1[i]-vec2[i])
    sum=math.sqrt(sum)
    return sum
