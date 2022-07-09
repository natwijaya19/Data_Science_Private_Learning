#%%
from datetime import datetime
import pandas_datareader as web
import datetime
# import pandas as pd

symbol = "GE"
channel_dr = "yahoo"
start_date = "2019-01-01"
end_date = datetime.date.today()

stock_df = web.DataReader("GE", "yahoo", start=start_date, end=end_date)

stock_df["Open"]


#%%
import datetime
date_now = datetime.datetime.now()
date_today = datetime.datetime.today()

