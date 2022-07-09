#%%
import platform
import sys
print("user current version: ", sys.version)

#%%
from platform import python_version

print("user current version: ", python_version())


#%%

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

rand_data= np.random.randint(low=-5,high=200, size=(10,4))
rand_df = pd.DataFrame(rand_data, columns=['col1', 'col2', 'col3', 'col4'])
print(rand_data)
print(rand_df)
print(rand_df)






