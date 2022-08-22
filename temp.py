from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override()  # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("ITC.BOM", period="max")

print(data)