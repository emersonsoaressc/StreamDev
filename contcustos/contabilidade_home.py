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
            st.write('Agora vamos dividir os gastos em DESPESAS FIXAS, DESPESAS VARIÁVEIS e INVESTIMENTOS')
            st.write('')
            tipo_despfixas = st.multiselect(
            'Selecione todas os gastos possíveis de forma realista!',
            ['Aluguel', 'Pensão', 'Alimentação', 'Energia Elétrica','Lazer', 'Educação', 'Vestimentas', 'Internet', 'Petshop', 'Água', 'Condomínio', 'Combustível'],['Alimentação'])
            despfixas = pd.DataFrame()
            nome_despfixas = []
            valor_despfixas = []
            for i in range(len(tipo_despfixas)):
                despfixa = tipo_despfixas[i] 
                valor_despfixa = st.number_input(f'{tipo_despfixas[i]}: ',min_value=None, value=0.00)
                nome_despfixas = append(despfixa,nome_despfixas)
                valor_despfixas = append(valor_despfixa, valor_despfixas)
            df_despfixas = pd.DataFrame(list(zip(nome_despfixas,valor_despfixas)), columns = ['Tipo de Despesas Fixas','Valor'])
            total_despfixas = df_despfixas['Valor'].sum()
            df_despfixas['%'] = df_despfixas['Valor']*100/total_despfixas
            st.write(df_despfixas)
            st.warning(f'O valor total das despesas fixas é de: {total_despfixas}')

        elif box_cont == 'Plano para Aposentadoria':
            st.write('Plano para Aposentadoria')   