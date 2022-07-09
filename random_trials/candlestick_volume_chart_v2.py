# %% prepare the data
import os
import pathlib

import pandas as pd

cwd = os.getcwd()
PV_DATA = pathlib.Path(cwd, "data", "TSLA.csv")
daily = pd.read_csv(PV_DATA, index_col=0, parse_dates=True)
daily.index.name = "Date"

daily.shape
daily.head(3)
daily.tail(3)

# %%
import mplfinance as mpf

mpf.plot(daily)

# %%

mpf.plot(daily, type="candle")
