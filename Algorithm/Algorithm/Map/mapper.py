def mapper(cent, datapoint):
    min = Find_dist(datapoint,cent[0])
    closest = cent[0]
    for i in range(1,len(cent)):
        curr = Find_dist(datapoint,cent[i])
        if curr < min:
            min = curr
            closest = cent[i]
#return key = centre, datapoint

    return closest,datapoint

