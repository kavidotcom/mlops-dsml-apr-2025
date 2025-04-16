import pandas as pd
import streamlit as st
import numpy as np
import yfinance as yf

st.title('Stock Market Analysis')
# st.header('Stock Price Analysis')
# st.subheader('Select a stock to analyze')
# st.text('This app allows you to analyze stock prices and visualize trends over time.')

start_date = st.date_input('Start date', format = 'YYYY-MM-DD')
end_date = st.date_input('End date', format = 'YYYY-MM-DD')

symbol = st.text_input('Enter stock symbol', 'AAPL')

data = yf.Ticker(symbol)
df = data.history(start=start_date, end=end_date)

st.dataframe(df)


col1, col2 = st.columns(2)

with col1:
    st.write('## Opening Price')
    st.line_chart(df['Open'])

with col2:
    st.write('## Closing Price')
    st.line_chart(df['Close'])