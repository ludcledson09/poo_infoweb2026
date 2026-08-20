import streamlit as st
from paciente import Paciente
from datetime import datetime, date

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        nascimento = st.date_input("Data de Nascimento", value = datetime(2000, 1, 1), \
                                    min_value = date(1900, 1, 1), \
                                    max_value=date.today(),\
                                    format="DD/MM/YYYY")
        nascimento = datetime.combine(nascimento, datetime.min.time())
        if st.button("idade"):
            x = Paciente(nome, cpf, telefone, nascimento)
            st.write(x.idade())

