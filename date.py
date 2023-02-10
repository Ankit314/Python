import pandas as pd
import numpy as np
d=pd.date_range('20221212',periods=8)
a1=pd.read_csv("F:/numpy/EXCEL2.csv")
a1=a1.set_index([d])
b=pd.DataFrame(a1,index=d)
c=a1.reindex(index=d[0:7],columns=list(a1.columns)+['E'])
c.loc[d[0]:d[4],'E']=1,2,3,4,5
c.isnull()
m=c.fillna(value=5)
print(m)

c.dropna()
print(c)
print(b)
print(d)
print(b.head())
print(b.tail())
print(b.info())
print(b.describe())
print(b.iloc[2:3,4:7])