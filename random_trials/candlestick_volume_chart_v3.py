#%%
import os
import pathlib
import pandas as pd

cwd = os.getcwd()
file_path = pathlib.Path(cwd, "data", "AAPL.CSV")
aapl_df = pd.read_csv(file_path, index_col=0, parse_dates=True)
dt_range = pd.date_range(start="2020-03-01", end="2020-03-31")
aapl_df = aapl_df[aapl_df.index.isin(dt_range)]
aapl_df.head()


#%%
print(file_path)

#%%
import cufflinks as cf
qf = cf.QuantFig(aapl_df, title="Apple Quant Figure", legend='top', name='GS')
qf.add_bollinger_bands()
qf.add_volume()
qf.iplot()

