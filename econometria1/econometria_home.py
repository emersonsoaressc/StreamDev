import streamlit as st
from econometria1.reglinearsimples.formulas import *
from econometria1.reglinearsimples.exercicios_rls import *
from econometria1.calc_regressao import calcRegressao


# Lista de temas e sub-temas
lista_temas = ['Regressão Linear']
lista_box_rls = ['Calculadora','Fórmulas Usadas']

# Função chamada
def econ():
    # Página principal do departamento de Econometria
    st.write('Página principal do departamento de Econometria')
    tema = st.sidebar.selectbox('Selecione o tema:', lista_temas)
    if tema == 'Regressão Linear':
        box_rls = st.sidebar.selectbox('Opções:', lista_box_rls)
        if box_rls == 'Calculadora':
            st.write('Calculadora de estimadores e parâmetros de confiabilidade')
            st.write(calcRegressao())
        elif box_rls == 'Fórmulas Usadas':
            st.write(imagemFormulas())