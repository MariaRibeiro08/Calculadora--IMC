import streamlit as st

#Criar a barra lateral
with st.sidebar:
    st.title("Calculadora IMC")
    st.header("O que é IMC")
    st.markdown("""O IMC, ou Índice de Massa Corporal, é um cálculo simples que permite avaliar se a pessoa está dentro do peso que é considerado ideal para a sua altura.""")
    #Linha com texto
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5
    - **Peso ideal**: IMC entre 18.5 e 24.9
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade mórbida**: IMC acima de 40
    """)


st.title("Calculadora IMC")

#Entrada de dados - peso altura
peso = st.number_input(label="Digite seu peso (Em Kg)", min_value=0.0, step=0.10, format="%.1f")

altura = st.number_input(label="Digite sua altura (Em metros)", min_value=0.0, step=0.10, format="%.2f")

#Criando botão

if st.button("Calcular"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal

        if imc < 18.5:
            classe = "Abaixo do peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29.9:
            classe = "Sobrepeso"
        elif imc < 40:
            classe = "Obesidade"
        else:
            classe = "Obesidade mórbida"

        st.success("Cálculo realizado com sucesso")

        #Escrever os vaores:
        st.write(f"Seu IMC é: {imc:.2f}")
        st.write(f"Classificação: {classe}")
        st.write(f"Comparação com IMC ideal (21.7): **{imc_delta:.2f}**")


        #Dividir a linha em duas colunas 
        col1, col2= st.columns(2)
        col1.metric("Classificação", classe, f"{imc_delta:.2f}", delta_color= "inverse")
        col2.metric("IMC", f"{imc:.2f}", f"{imc_delta:.2f}", delta_color= "off")

        #Criar uma linha

        st.divider()
        st.image("./imc.jfif")



    else:
        #mostrar mensagem de erro 
        st.error("Por favor, insira um valor válido para peso e altura.")