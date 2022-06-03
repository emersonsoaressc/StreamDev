from numpy import append, var
import streamlit as st 
import pandas as pd 

def calcRegressao():
    st.write('Primeiramente vamos obter os dados. Escolha umas das opções abaixo:')
    tipo_dados = st.selectbox('Qual o tipo de obtenção dos dados?',['Tabela de dados','Somatórios de dados'])
    if tipo_dados == 'Somatórios de dados':
        st.write('')
    else:
        n_variaveis = st.number_input('Quantas váriaveis possui?:',step=1, min_value=2, max_value=10)
        var_X = pd.DataFrame()
        var_Y = pd.DataFrame()
        dados = pd.DataFrame()


        lstY = (st.text_area(f'Coloque aqui os valores para a variável Y separados por ENTER')).splitlines()
        lstY_num = [float(string) for (string) in lstY]
        listaY = pd.DataFrame(lstY_num, columns=[f'Y'])
        listaY[f'Y²'] = listaY*listaY
        var_Y = pd.concat([var_Y,listaY], axis=1)
        eY = [sum(lstY_num)]
        eYquad = [sum(listaY[f'Y²'])]
        somatorioY = pd.DataFrame(eY,columns=[f'EY'])
        somatorioYquad = pd.DataFrame(eYquad,columns=[f'EY²'])
        n = [len(listaY.index)]
        n = pd.DataFrame(n, columns=['n'])
        dados = pd.concat([dados,n,somatorioY,somatorioYquad], axis=1)
        dados['Ybarra'] = dados['EY']/dados['n']

        for i in range(n_variaveis-1):
            lst = (st.text_area(f'Coloque aqui os valores para a variável X{i+2} separados por ENTER')).splitlines()
            lst_num = [float(string) for (string) in lst]
            listaX = pd.DataFrame(lst_num, columns=[f'X{i+2}'])
            listaX[f'X{i+2}²'] = listaX*listaX
            var_X = pd.concat([var_X,listaX], axis=1)
            eX = [sum(lst_num)]
            eXquad = [sum(listaX[f'X{i+2}²'])]
            somatorioX = pd.DataFrame(eX,columns=[f'EX{i+2}'])
            somatorioXquad = pd.DataFrame(eXquad,columns=[f'EX{i+2}²'])
            dados = pd.concat([dados,somatorioX,somatorioXquad], axis=1)
        
        
        st.write(var_X,var_Y)
        st.write(dados)

        st.write('Pronto, agora que temos nossa tabela de dados, vamos calcular os estimadores')
        st.write('O primeiro passo é ')

            




