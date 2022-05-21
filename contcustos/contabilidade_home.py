import pandas as pd 
from numpy import append
import streamlit as st


def contc():
    # Lista de temas e sub-temas
    lista_temas = ['Planejamento Financeiro Pessoal']
    lista_box_cont = ['Análise sobre Orçamento Pessoal','Conceito', 'Plano para Aposentadoria']
    # Função chamada
    tema = st.sidebar.selectbox('Selecione o tema:', lista_temas)
    if tema == 'Planejamento Financeiro Pessoal':
        box_cont = st.sidebar.selectbox('Opções:', lista_box_cont)
        if box_cont == 'Conceito':
            st.write('Página principal sobre Contabilidade de Custos')
            st.write('Conceito sobre Planejamento Financeiro Pessoal')
            st.text('texto aqui!')
        elif box_cont == 'Análise sobre Orçamento Pessoal':
            st.header('Análise sobre Orçamento Pessoal')
            st.subheader('Aqui será possível desenvolver o orçamento mensal pessoal ou familiar de forma simples e objetiva. Para tal vamos seguir alguns passos que vão orientar todo o processo.')
            st.subheader('PASSO 1 - RECEITAS')
            tipo_receitas = st.multiselect(
            'Selecione todas as receitas possíveis de forma realista!',
            ['Salário', 'Pensão', 'Renda Extra', 'Mesada'],['Salário'])
            receitas = pd.DataFrame()
            nome_receitas = []
            valor_receitas = []
            for i in range(len(tipo_receitas)):
                receita = tipo_receitas[i] 
                valor_receita = st.number_input(f'{tipo_receitas[i]}: ',min_value=None, value=0.00)
                nome_receitas = append(receita,nome_receitas)
                valor_receitas = append(valor_receita, valor_receitas)
            df_receitas = pd.DataFrame(list(zip(nome_receitas,valor_receitas)), columns = ['Tipo de Receita','Valor'])
            total_receitas = df_receitas['Valor'].sum()
            df_receitas['%'] = df_receitas['Valor']*100/total_receitas
            st.write(df_receitas)
            st.warning(f'O valor total das receitas é de: {total_receitas}')
            st.subheader('PASSO 2 - GASTOS')
            tipo_gastos = st.multiselect(
            'Selecione todas os gastos possíveis de forma realista!',
            ['Aluguel', 'Pensão', 'Alimentação', 'Energia Elétrica','Lazer', 'Educação', 'Vestimentas', 'Internet', 'Petshop', 'Água', 'Condomínio', 'Combustível'],['Alimentação'])
            gastos = pd.DataFrame()
            nome_gastos = []
            valor_gastos = []
            for i in range(len(tipo_gastos)):
                gasto = tipo_gastos[i] 
                valor_gasto = st.number_input(f'{tipo_gastos[i]}: ',min_value=None, value=0.00)
                nome_gastos = append(gasto,nome_gastos)
                valor_gastos = append(valor_gasto, valor_gastos)
            df_gastos = pd.DataFrame(list(zip(nome_gastos,valor_gastos)), columns = ['Tipo de Gasto','Valor'])
            total_gastos = df_gastos['Valor'].sum()
            df_gastos['%'] = df_gastos['Valor']*100/total_gastos
            st.write(df_gastos)
            st.warning(f'O valor total dos gastos é de: {total_gastos}')

        elif box_cont == 'Plano para Aposentadoria':
            st.write('Plano para Aposentadoria')   