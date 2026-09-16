import streamlit as st
import pandas as pd
import time
from service import Service

class ManterEndereçoUI:
    def main():
        st.header("Cadastro de Endereço")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        with tab1: ManterEndereçoUI.listar()
        with tab2: ManterEndereçoUI.inserir()
        with tab3: ManterEndereçoUI.atualizar()
        with tab4: ManterEndereçoUI.excluir()
    def listar():
     endereços = Service.endereço_listar()
     if len(endereços) ==0: st.write("Nenhum endereço cadastrado")
     else:
        list_dic = []
        for obj in endereços: list_dic.append(obj.to_json())
        df = pd.DataFrame(list_dic)
        st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        endereço = st.text_input("Informe o endereço")
        id_cliente = st.text_input("Informe o id_cliente")
        if st.button("Inserir"):
            Service.endereço_inserir(nome, endereço, int(id_cliente))
            st.success("Endereço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        endereços = Service.cliente_listar()
        if len(endereços) == 0: st.write("Nenhum endereço cadastrado")
        else:
            op = st.selectbox("Atualização de Endereços", endereços)
            nome = st.text_input("Novo nome", op.get_nome())
            endereço = st.text_input("Novo endereço", op.get_endereço())
            id_cliente = st.text_input("Novo id_cliente", op.get_id_cliente())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.enderço_atualizar(id,nome, endereço, int(id_cliente) )
                st.success("Endereço atualizado com sucesso")
    def excluir():
        endereços = Service.cliente_listar()
        if len(endereços) == 0: st.write("Nenhum endereço cadastrado")
        else:
            op = st.selectbox("Exclusão de Endereços",endereços )
            if st.button("Excluir"):
                id = op.get_id()
                Service.endereço_excluir(id)
                st.success("Endereço excluído com sucesso")
