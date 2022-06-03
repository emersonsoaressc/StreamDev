from numpy import append, var
import streamlit as st 

def calcRegressao():
    st.write('Primeiramente vamos obter os dados. Escolha umas das opções abaixo:')
    tipo_dados = st.selectbox('Qual o tipo de obtenção dos dados?',['Tabela de dados','Somatórios de dados'])
    if tipo_dados == 'Tabela de dados':
        st.write('')
    else:
        n_variaveis = st.number_input('Quantas váriaveis possui?:',step=1, min_value=2, max_value=10)
        var_x = []

        for i in n_variaveis:
            v = i
            var_x = append(i,var_x)
        st.write(var_x)


