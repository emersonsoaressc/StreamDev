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

def backtest_stock(tickers='BBAS3.SA',benchmark='^BVSP',strategy=''):
    try:
        dados = vbt.YFData.download(
            tickers, 
            benchmark=benchmark,
            missing_index='drop',
            start='2000-01-01', 
            interval='1d').get('Close')
        retornos = dados/dados.iloc[0]
    except:
        dados = ''
        retornos = ''
    return dados, retornos

  