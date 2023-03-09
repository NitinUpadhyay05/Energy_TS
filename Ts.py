 # AEP 


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import plotly.express as px
import plotly.graph_objects as go
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
import streamlit as st

color_pal = sns.color_palette()
plt.style.use('fivethirtyeight')

# DATA OF COMPANY AEP
df_AEP = pd.read_csv("D:/newTS/AEP_hourly.csv")
df_AEP.set_index('Datetime')
df_AEP.index = pd.to_datetime(df_AEP.index)
df_AEP.Datetime = pd.to_datetime(df_AEP.Datetime)


# DATA OF COMPANY PJME

df_PJME = pd.read_csv("D:/newTS/PJME_hourly.csv")
df_PJME.set_index('Datetime')
df_PJME.index = pd.to_datetime(df_PJME.index)
df_PJME.Datetime = pd.to_datetime(df_PJME.Datetime)


# DATA OF COMPANY DAYTON

df_DAYTON = pd.read_csv("D:/newTS/DAYTON_hourly.csv")
df_DAYTON.set_index('Datetime')
df_DAYTON.index = pd.to_datetime(df_DAYTON.index)
df_DAYTON.Datetime = pd.to_datetime(df_DAYTON.Datetime)


# DATA OF COMPANY PJMW

df_PJMW = pd.read_csv("D:/newTS/PJMW_hourly.csv")
df_PJMW.set_index('Datetime')
df_PJMW.index = pd.to_datetime(df_PJMW.index)
df_PJMW.Datetime = pd.to_datetime(df_PJMW.Datetime)


# DATA OF COMPANY DOM

df_DOM = pd.read_csv("D:/newTS/DOM_hourly.csv")
df_DOM.set_index('Datetime')
df_DOM.index = pd.to_datetime(df_DOM.index)
df_DOM.Datetime = pd.to_datetime(df_DOM.Datetime)


selected_comp = st.selectbox("Select the company", ["AEP", "PJME", "DAYTON", "PJMW", "DOM"])

if selected_comp is not None:
    if selected_comp == "AEP":
        # Visualization of data
        st.plotly_chart(px.scatter(df_AEP,x = 'Datetime',y = 'AEP_MW',title='AEP Energy usage in MW'))

        train = df_AEP.loc[df_AEP.Datetime < '2015-01-01']
        test = df_AEP.loc[df_AEP.Datetime >= '2015-01-01']
        
        from_date = st.date_input("Select from date")
        end_Date = st.date_input("Select till date")

        date_show_btn = st.button("Show data")

        if date_show_btn:
            selected_date = df_AEP.loc[(df_AEP.Datetime > str(from_date)) & (df_AEP.Datetime <= str(end_Date))]
            st.line_chart(plt.plot(selected_date['Datetime'], selected_date['AEP_MW']))
            