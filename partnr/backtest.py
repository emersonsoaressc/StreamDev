import pandas as pd 
from numpy import append
import streamlit as st
import vectorbt as vbt
from partnr.fc_partnr import *
import plotly.express as px
import seaborn as sns
sns.set()


def layout_page():
    stocks = st.multiselect('Escolha os ativos', ['BBAS3.SA','ABEV3.SA','VALE3.SA'])
    stocks.append('^BVSP')
    dados, retornos = backtest_stock(tickers=stocks)
    st.write(px.line(retornos)) 
    st.write(dados)
    #st.line_chart(retornos,width=100,height=100)
