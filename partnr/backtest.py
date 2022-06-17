import pandas as pd 
from numpy import append
import streamlit as st
import vectorbt as vbt
from partnr.fc_partnr import *
import seaborn as sns
sns.set()


def layout_page():
    dados = backtest_stock()
    st.write('Hello World!') 
    st.write(dados.plot().show())