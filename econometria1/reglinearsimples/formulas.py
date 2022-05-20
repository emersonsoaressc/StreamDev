import streamlit as st

# Fórmulas de Regressão Linear Simples
def imagemFormulas():
    st.image('econometria1/img/formulas_econometria_01.jpg')

# Obter estimadores B1 e B2 com somas dadas pela questão
def estimadores(n, EX, EY, EXX,EYY, EXY):
    beta2e = (n*EXY-EX*EY)/(n*EXX-(EX^2))
    beta1e = (EY/n)-beta2e*(EX/n)
    return beta2e, beta1e

