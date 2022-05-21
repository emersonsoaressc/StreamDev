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
            st.write('Agora vamos dividir os gastos em DESPESAS FIXAS, DESPESAS VARIÁVEIS e DESPESAS FINANCEIRAS')
            st.write('')
            st.subheader('Despesas Fixas')
            tipo_despfixas = st.multiselect(
            'Selecione todas as despesas fixas possíveis de forma realista!',
            ['Aluguel', 'Pensão', 'Educação', 'Internet', 'Petshop', 'Combustível', 'Academia', 'Inglês'],['Aluguel'])
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
            df_despfixas['% sobre Receitas'] = (df_despfixas['Valor']*100/total_receitas)
            df_despfixas = df_despfixas.sort_values(by=['% sobre Receitas'], ascending=False)
            st.write(df_despfixas)
            st.warning(f'O valor total das despesas fixas é de: {total_despfixas}')
            st.warning(f'Isto corresponde a {(total_despfixas*100/total_receitas):.2f}% das receitas totais')
            st.subheader('Despesas Variáveis')
            tipo_despvariaveis = st.multiselect(
            'Selecione todas as despesas variáveis possíveis de forma realista!',
            ['Alimentação', 'Energia Elétrica', 'Condomínio', 'Combustível', 'Lazer', 'Cabeleireiro', 'Transporte Coletivo', 'Recarga de Celular'],['Alimentação'])
            despvariaveis = pd.DataFrame()
            nome_despvariaveis = []
            valor_despvariaveis = []
            for i in range(len(tipo_despvariaveis)):
                despvariavel = tipo_despvariaveis[i] 
                valor_despvariavel = st.number_input(f'{tipo_despvariaveis[i]}: ',min_value=None, value=0.00)
                nome_despvariaveis = append(despvariavel,nome_despvariaveis)
                valor_despvariaveis = append(valor_despvariavel, valor_despvariaveis)
            df_despvariaveis = pd.DataFrame(list(zip(nome_despvariaveis,valor_despvariaveis)), columns = ['Tipo de Despesas Variáveis','Valor'])
            total_despvariaveis = df_despvariaveis['Valor'].sum()
            df_despvariaveis['% sobre Receitas'] = (df_despvariaveis['Valor']*100/total_receitas)
            df_despvariaveis = df_despvariaveis.sort_values(by=['% sobre Receitas'], ascending=False)
            st.write(df_despvariaveis)
            st.warning(f'O valor total das despesas variáveis é de: {total_despvariaveis}')
            st.warning(f'Isto corresponde a {(total_despvariaveis*100/total_receitas):.2f}% das receitas totais')
            st.subheader('Despesas Financeiras')
            tipo_despfinanceiras = st.multiselect(
            'Selecione todas as despesas financeiras possíveis de forma realista!',
            ['Financiamento de Veículos', 'Financiamento de Imóvel', 'Empréstimos'],['Empréstimos'])
            despfinanceiras = pd.DataFrame()
            nome_despfinanceiras = []
            valor_despfinanceiras = []
            for i in range(len(tipo_despfinanceiras)):
                despfinanceira = tipo_despfinanceiras[i] 
                valor_despfinanceira = st.number_input(f'{tipo_despfinanceiras[i]}: ',min_value=None, value=0.00)
                nome_despfinanceiras = append(despfinanceira,nome_despfinanceiras)
                valor_despfinanceiras = append(valor_despfinanceira, valor_despfinanceiras)
            df_despfinanceiras = pd.DataFrame(list(zip(nome_despfinanceiras,valor_despfinanceiras)), columns = ['Tipo de Despesas Financeiras','Valor'])
            total_despfinanceiras = df_despfinanceiras['Valor'].sum()
            df_despfinanceiras['% sobre Receitas'] = (df_despfinanceiras['Valor']*100/total_receitas)
            df_despfinanceiras = df_despfinanceiras.sort_values(by=['% sobre Receitas'], ascending=False)
            st.write(df_despfinanceiras)
            st.warning(f'O valor total das despesas financeiras é de: {total_despfinanceiras}')
            st.warning(f'Isto corresponde a {(total_despfinanceiras*100/total_receitas):.2f}% das receitas totais')
            st.subheader('PASSO 3 - INVESTIMENTOS')
            st.write('Agora vamos incluir os aportes realizados para os investimentos')
            st.write('')
            st.subheader('Investimentos')
            tipo_investimentos = st.multiselect(
            'Selecione todas aportes mensais nos tipos de investimentos de forma realista!',
            ['Poupança', 'TD Pré-fixado', 'TD Selic', 'TD Ipca +', 'CDB', 'LCI', 'LCA', 'Fundos Imobiliários', 'Ações Nacionais', 'Ações Americanas', 'Dólar', 'Ouro', 'Prata', 'Bitcoins', 'Outras Criptomoedas', 'Reits'],['Poupança'])
            investimentos = pd.DataFrame()
            nome_investimentos = []
            valor_investimentos = []
            for i in range(len(tipo_investimentos)):
                investimento = tipo_investimentos[i] 
                valor_investimento = st.number_input(f'{tipo_investimentos[i]}: ',min_value=None, value=0.00)
                nome_investimentos = append(investimento,nome_investimentos)
                valor_investimentos = append(valor_investimento, valor_investimentos)
            df_investimentos = pd.DataFrame(list(zip(nome_investimentos,valor_investimentos)), columns = ['Tipo de Investimento','Valor'])
            total_investimentos = df_investimentos['Valor'].sum()
            df_investimentos['% sobre Receitas'] = (df_investimentos['Valor']*100/total_receitas)
            df_investimentos = df_investimentos.sort_values(by=['% sobre Receitas'], ascending=False)
            st.write(df_investimentos)
            st.warning(f'O valor total das despesas fixas é de: {total_investimentos}')
            st.warning(f'Isto corresponde a {(total_investimentos*100/total_receitas):.2f}% das receitas totais')
            df_dre = pd.DataFrame()
            df_dre['Demonstrativo Mensal'] = ['Receitas','Despesas Fixas', 'Despesas Variáveis', 'Despesas Financeiras', 'Investimentos']
            df_dre['Valor'] = [total_receitas, total_despfixas, total_despvariaveis, despfinanceiras, total_investimentos]
            st.write(df_dre)

        elif box_cont == 'Plano para Aposentadoria':
            st.write('Plano para Aposentadoria')   