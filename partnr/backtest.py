import pandas as pd 
from numpy import append
import streamlit as st
import vectorbt as vbt
from partnr.fc_partnr import *
import seaborn as sns
sns.set()


def layout_page():
    stocks = st.multiselect('Escolha os ativos', ['BBAS3.SA','ABEV3.SA','VALE3.SA'])
    dados, retornos = backtest_stock(tickers=stocks)
    st.write(type(stocks)) 
    st.write(dados)
    st.write(retornos)