import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import pandas_datareader as data


import streamlit as st



start = '2010/01/01'
end = '2019/12/01'

st.title('Yahoo Stock Exchange')


user_input = st.text_input('Enter Stock Company', 'TSLA')
df = data.DataReader(user_input, 'yahoo', start, end)

#Data Describe
st.subheader('Data from 2010-2019')
st.write(df.describe())


#graph
st.subheader('Closing price vs Time Chart')
flg = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(flg)


#100MA
st.subheader('closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
flg = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(flg)


#200MA
st.subheader('closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
flg = plt.figure(figsize = (12,6))
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'y')
st.pyplot(flg)