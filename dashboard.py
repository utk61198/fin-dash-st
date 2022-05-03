import pandas as pd
import numpy as np
from pyparsing import col
from requests import options
import yfinance as yf
import streamlit as st
st.set_page_config(layout="wide")
'''
# Financial Dashboard
'''

col1, col2 = st.columns([2,1])

with col1:
    ticker=st.text_input('Enter the stock ticker')
    period=st.select_slider('Select time period',options=["1mo","3mo","6mo","1y","3y","5y","max"])
    stock=yf.Ticker(ticker.upper())

    x_axis=stock.history(period).index
    y_axis=stock.history(period)['Close']
    params=[]
    values=[]
    for key,value in stock.info.items():
        params.append(key)
        values.append(value)

    if stock.info['longName']:
        st.write(stock.info['longName'])
    st.line_chart(pd.DataFrame(y_axis,x_axis),width=100)

with col2:
    st.dataframe(pd.DataFrame(data=np.array(values),index=params,columns=["Company parameters"]).astype(str))
