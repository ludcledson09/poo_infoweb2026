from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manteratendimentoui import ManterAtendimentoUI
from templates.manterendereçoui import ManterEndereçoUI
from templates.manterprofissionalui import ManterProfissionalUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários","Atendimentos","Endereços","Profissionais"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()
        if op == "Endereços": ManterEndereçoUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        

IndexUI.main()
