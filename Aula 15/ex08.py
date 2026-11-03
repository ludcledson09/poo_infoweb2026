class ManterServicoUI:
 def inserir():
   descrição = st.text_input("Informe a descrição")
   valor = st.text_input("Informe o valor (R$)")
   if st.button("Inserir"):
   try:
      Service.servico_inserir(descrição, float(valor))
      st.success("Serviço inserido com sucesso")
  except ValueError:
    st.write("Descrição e/ou valor inválidos")

