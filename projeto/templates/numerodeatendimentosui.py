import streamlit as st
import pandas as pd
import time
from service import Service

class NumerodeAtendimentosUI:
    def main():
        st.header("Numero de Atendimentos")

        profissionais = Service.profissional_listar()
        if len(profissionais) ==0: st.write("Nenhum profissional cadastrado")
        else:
          list_dic = []
          for obj in profissionais: list_dic.append(obj.to_json())
          df = pd.DataFrame(list_dic)
          st.dataframe(df)
