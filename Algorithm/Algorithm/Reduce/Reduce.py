def Reduce(d1,center,new_centers):
        for i in range(0,len(d1)):
            a= d1[i];
            for j in range(0,len(center)):
                if a == center[j]:
                    center[j]=new_centers[i]
        return center
