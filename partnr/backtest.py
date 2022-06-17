import pandas as pd 
from numpy import append
import streamlit as st
import vectorbt as vbt
import seaborn as sns
sns.set()


def layout_page():
    st.write('Hello World!')    

class Strategy():
    def estrategia1():
        pass
    pass

def backtest_stock(ticker,benchmark,strategy):
    dados = vbt.YFData.download(
        ['BOVA11.SA','BBAS3.SA'], 
        missing_index='drop',
        start='2000-01-01', 
        interval='1d').get('Close')
    dados = dados/dados.iloc[0]
    return dados

