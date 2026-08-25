import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.header("Cadastro de Servicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    def listar():
     servicos = Service.servico_listar()
     if len(servicos) ==0: st.write("Nenhum servico cadastrado")
     else:
        list_dic = []
        for obj in servicos: list_dic.append(obj.to_json())
        df = pd.DataFrame(list_dic)
        st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descricao")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            Service.servico_inserir(descricao, float(valor))
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum servico cadastrado")
        else:
            op = st.selectbox("Atualização de Servicos", servicos)
            descricao = st.text_input("Nova descricao", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                Service.servicos_atualizar(descricao,float(valor))
                st.success("Servico atualizado com sucesso")
    def excluir():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum servico cadastrado")
        else:
            op = st.selectbox("Exclusão de Servicos", servicos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("Servico excluído com sucesso")
