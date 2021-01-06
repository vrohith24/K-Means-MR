def mapper(cent,center,datapoint, datapoint1):
    min1 = Find_dist(datapoint1,cent[0])
    closest = cent[0]
    for i in range(1,len(cent)):
        curr = Find_dist(datapoint1,cent[i])
        if curr < min1:
            min1 = curr
            closest = cent[i]
    center.append(closest)
    datapoint.append(datapoint1)
    return center,datapoint
