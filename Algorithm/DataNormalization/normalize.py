def simpleF(p1,p2):
#change column values
    return f.udf(lambda col: int(((col - p2)/ (p1-p2) )*100), IntegerType())
def normalize(df):
    result = df.collect()
    res=df
    i=0
    for feature_name in df.columns:
        fn="max("+feature_name+")"
        fn1="min("+feature_name+")"
#get maximum and minimum
        max_value = df.agg({feature_name: "max"}).collect()[0][fn]
        min_value = df.agg({feature_name: "min"}).collect()[0][fn1]
        #min_value=0;max_value=100;
        res=res.withColumn(feature_name, simpleF(max_value,min_value)(feature_name))
    return res
