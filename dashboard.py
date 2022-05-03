import pandas as pd
import numpy as np
from requests import options
import yfinance as yf
import streamlit as st



'''
# Financial Dashboard
'''

ticker=st.text_input('Enter the stock ticker')
period=st.select_slider('Select time period',options=["1mo","3mo","6mo","1y","3y","5y","max"])
st.write(ticker)
stock=yf.Ticker(ticker.upper())
x_axis=stock.history(period).index
y_axis=stock.history(period)['Close']
st.line_chart(pd.DataFrame(y_axis,x_axis))