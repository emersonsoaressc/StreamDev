import streamlit as st
import pandas as pd
import numpy as np
from econometria1.econometria_home import econ
from contcustos.contabilidade_home import contc
from partnr.backtest import layout_page


#######################################
# CONSTRUÇÃO DA BARRA LATERAL COM LOGO
#######################################
def barraLateral():
    st.sidebar.image('img/logo.jpg')
    st.sidebar.write('Olá, este app tem por finalidade dar vida a vários mini-projetos ligados a diversos conteúdos.')
    #######################################
    # ESCOLHA DO DEPARTAMENTO
    #######################################
    departamentos = ['PARTNR','CONTABILIDADE DE CUSTOS', 'ECONOMETRIA 1']
    select_depto = st.sidebar.selectbox('Selecione o departamento:',departamentos)
    #######################################
    # SUB-TÓPICOS DE ECONOMETRIA 1
    #######################################
    if select_depto == 'PARTNR':
        st.write(layout_page())
    if select_depto == 'ECONOMETRIA 1':
        st.write(econ())
    if select_depto == 'CONTABILIDADE DE CUSTOS':
        st.write(contc())    