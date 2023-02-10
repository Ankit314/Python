import pandas as pd
import numpy as np
d=pd.date_range('20221212',periods=8)
df1=pd.Series(np.random.random(18),index=d)
 
print(df1)
