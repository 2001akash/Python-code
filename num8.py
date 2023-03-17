import pandas as pd
import numpy as np
data = np.array(['a','b''c'])
s1= pd.Series(data, index=[100, 101, 102])
print(s1)