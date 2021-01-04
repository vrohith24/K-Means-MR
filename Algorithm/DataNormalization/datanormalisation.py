#read data
def datanormalization()
    df3 = spark.read.options(header='True', delimiter=',').csv("/Users/vrohith/Downloads/data.csv")
    df3.head()

#select Features
    df=df3.select("1961","1983","2015")

#convert to decimal Type
    df = df.withColumn("1961",df["1961"].cast(DecimalType()))
    df = df.withColumn("1983",df["1983"].cast(DecimalType()))
    df = df.withColumn("2015",df["2015"].cast(DecimalType()))

    df
    df.show()

#replacing null with mean

    df_stats = df.select(_mean(col('1961')).alias('mean1'),_mean(col('1983')).alias('mean2'),_mean(col('2015')).alias('mean3')).collect()

    m1=df_stats[0]['mean1']
    m2=df_stats[0]['mean2']
    m3=df_stats[0]['mean3']

    print(m1,m2,m3)

    df1=df.na.fill({'1961': m1, '1983': m2,'2015': m3 })
    df1.show()
    #to have unique values
    #df1=df1.distinct()

#To replace null with 0

    data=df.na.fill(0)
    data.show()
    #to have unique values
    #data=data..distinct()

#Normalisation of desired data
    #calculating dimensions dim=2||3
    dim=len(df.columns)
    #drop null values
    df1=df.dropna()
#get normalised data
    df1=normalize(df1)
return df1
