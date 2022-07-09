# %%
import datetime

import pandas_datareader as web
import plotly.graph_objects as go
from plotly.subplots import make_subplots

symbol = "TSLA"
channel_dr = "yahoo"
start_date = "2019-01-01"
end_date = datetime.date.today()

stock_df = web.DataReader("GE", "yahoo", start=start_date, end=end_date)

# %%
figure = make_subplots(specs=[[{"secondary_y": True}]])

figure.add_trace(go.Candlestick(
    x=stock_df.index,
    low=stock_df["Low"],
    high=stock_df["High"],
    close=stock_df["Close"]),
    secondary_y=True)

figure.add_trace(go.Bar(x=stock_df.index, y=stock_df["Volume"]),
                 secondary_y=False)

figure.update_layout(
    title="TSLA",
    yaxis_title="TSLA Volume/Price",
    xaxis_title="Date"
)


#%%
stock_df_index = stock_df.index