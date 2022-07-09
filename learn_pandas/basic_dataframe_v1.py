#%%
from pathlib import Path
import os
import pandas as pd

#%%

home_dir = Path.home()
home_dir

#%%
cwd = Path.cwd()
cwd

#%%
# curr_file = Path(_file_)
# curr_file


#%%
one_above = Path.cwd().parents[0]
one_above

#%%

joined_path = cwd/'data'
joined_path


#%%
cwd  = Path.cwd
print(cwd)
DATASET_FILE_PATH = os.path.join('learn_pandas','data','earthquakes.csv')
print(DATASET_FILE_PATH)

df = pd.read_csv(DATASET_FILE_PATH)
df

df.head(10)
#%%

#%%
cwd  = Path.cwd
print(cwd)


