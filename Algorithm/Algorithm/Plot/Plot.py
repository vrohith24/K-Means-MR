if dim == 2:
    
    for i in range(len(dc+dp)):
        if data_n.iloc[i,2]==1.0:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='b',marker='.');
        elif data_n.iloc[i,2]==2.0 :
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='g',marker='.');
        elif data_n.iloc[i,2]==3.0:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='r',marker='+');
        elif data_n.iloc[i,2]==4.0:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='c',marker='*');
        elif data_n.iloc[i,2]==5:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='m',marker='.');
        elif data_n.iloc[i,2]==6:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='y',marker='o');
        elif data_n.iloc[i,2]==7:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1],c='k',marker='o');
        elif data_n.iloc[i,2]==8:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='m',marker='.');
        elif data_n.iloc[i,2]==9:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1],c='y',marker='.');
        elif data_n.iloc[i,2]==10:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='r',marker='.');
        elif data_n.iloc[i,2]==11:
            plt.plot(data_n.iloc[i, 0],     data_n.iloc[i,1] ,c='g',marker='.');


else:

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.set_xlabel('1961')
    ax.set_ylabel('1983')
    ax.set_zlabel('2015')
    for i in range(len(dc+dp)):
        if data_n.iloc[i,3]==1:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='b',marker='o');
        elif data_n.iloc[i,3]==2:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='m',marker='o');
        elif data_n.iloc[i,3]==3:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='y',marker='o');
        elif data_n.iloc[i,3]==4:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2]  ,c='r',marker='o');
        elif data_n.iloc[i,3]==5:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2]  ,c='c',marker='o');
        elif data_n.iloc[i,3]==6:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='g',marker='+');
        elif data_n.iloc[i,3]==7:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='y',marker='<');
        elif data_n.iloc[i,3]==8:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2]  ,c='k',marker='o');
        elif data_n.iloc[i,3]==9:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='m',marker='.');
        elif data_n.iloc[i,3]==10:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='y',marker='.');
        elif data_n.iloc[i,3]==11:
            ax.scatter(data_n.iloc[i, 0], data_n.iloc[i,1] ,data_n.iloc[i,2] ,c='r',marker='.');


plt.show()
#no.of points in each cluster
d={};
r=list(data_n.iloc[:,dim]);
for i in r:
    if i in d:
        d[i]+=1;
    else:
        d[i]=1;

print(d)
