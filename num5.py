import pandas as pd
import numpy as np
data= np.array(['abc','xyz','klm'])
data
type(data)
data.dtype
series1=pd.Series(data,index=[100, 101, 102])
series1
type(series1)
data1=np.array([['Alex',10], ['Bob',12], ['Rahul',13]])
print (data1)