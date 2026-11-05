def inserir(self, obj):
    # gerar um novo id com o maior valor existente mais um
    id = 0
    if len(self._objetos) > 0:
        for aux in self._objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        self._objetos.append(obj)
        self._salvar()