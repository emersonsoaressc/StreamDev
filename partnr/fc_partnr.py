import pandas as pd 
from numpy import append
import streamlit as st
import vectorbt as vbt
import seaborn as sns
sns.set()


class Strategy():
    def estrategia1():
        pass
    pass

def backtest_stock(ticker='BBAS3.SA',benchmark='^BVSP',strategy=''):
    dados = vbt.YFData.download(
        ['BOVA11.SA','BBAS3.SA'], 
        missing_index='drop',
        start='2000-01-01', 
        interval='1d').get('Close')
    dados = dados/dados.iloc[0]
    return dados

def layout_page():
    st.write('Hello World!')   
    st.write(backtest_stock()) 