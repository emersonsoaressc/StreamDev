import streamlit as st
from econometria1.reglinearsimples.formulas import *
from econometria1.reglinearsimples.exercicios_rls import *


# Lista de temas e sub-temas
lista_temas = ['Regressão Linear Simples', 'Regressão Múltipla']
lista_box_rls = ['Conceito','Fórmulas Usadas', 'Exercício 1 - AV1']

# Função chamada
def econ():
    # Página principal do departamento de Econometria
    st.write('Página principal do departamento de Econometria')
    tema = st.sidebar.selectbox('Selecione o tema:', lista_temas)
    if tema == 'Regressão Linear Simples':
        box_rls = st.sidebar.selectbox('Opções:', lista_box_rls)
        if box_rls == 'Conceito':
            st.write('Conceito sobre REGRESSÃO LINEAR SIMPLES')
        elif box_rls == 'Fórmulas Usadas':
            st.write(imagemFormulas())
        elif box_rls == 'Exercício 1 - AV1':
            st.write(ex_rls001())