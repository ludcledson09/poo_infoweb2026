import uuid
from datetime import datetime

class MoedaFicticia:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo
        self.saldos = {}  # Armazena saldos por usuário
        self.transacoes = []  # Histórico de transações

    def criar_usuario(self):
        """Cria um novo usuário com saldo inicial zero."""
        user_id = str(uuid.uuid4())
        self.saldos[user_id] = 0.0
        return user_id

    def adicionar_saldo(self, user_id, valor):
        """Adiciona saldo ao usuário."""
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        if user_id not in self.saldos:
            raise KeyError("Usuário não encontrado.")
        self.saldos[user_id] += valor
        self.transacoes.append({
            "de": "Sistema",
            "para": user_id,
            "valor": valor,
            "data": datetime.now()
        })

    def transferir(self, de_id, para_id, valor):
        """Transfere saldo entre usuários."""
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        if de_id not in self.saldos or para_id not in self.saldos:
            raise KeyError("Usuário não encontrado.")
        if self.saldos[de_id] < valor:
            raise ValueError("Saldo insuficiente.")
        
        self.saldos[de_id] -= valor
        self.saldos[para_id] += valor
        self.transacoes.append({
            "de": de_id,
            "para": para_id,
            "valor": valor,
            "data": datetime.now()
        })

    def saldo(self, user_id):
        """Retorna o saldo do usuário."""
        if user_id not in self.saldos:
            raise KeyError("Usuário não encontrado.")
        return self.saldos[user_id]

    def historico(self):
        """Retorna o histórico de transações."""
        return self.transacoes


# ===== Exemplo de uso =====
if __name__ == "__main__":
    moeda = MoedaFicticia("Boró", "BRO")

    # Criar dois usuários
    usuario1 = moeda.criar_usuario()
    usuario2 = moeda.criar_usuario()

    # Adicionar saldo ao usuário 1
    moeda.adicionar_saldo(usuario1, 100)

    # Transferir para usuário 2
    moeda.transferir(usuario1, usuario2, 25)

    # Mostrar saldos
    print(f"Saldo usuário 1: {moeda.saldo(usuario1)} {moeda.simbolo}")
    print(f"Saldo usuário 2: {moeda.saldo(usuario2)} {moeda.simbolo}")

    # Mostrar histórico
    for t in moeda.historico():
        print(t)