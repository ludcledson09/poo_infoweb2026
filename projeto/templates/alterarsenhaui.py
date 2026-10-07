import streamlit as st
from service import Service
import time

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("nome", op.get_nome(), disabled = True)
        email = st.text_input("e-mail", op.get_email(), disabled = True)
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            Service.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Dados atualizados com sucesso")
            time.sleep(2)
            st.rerun()