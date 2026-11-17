from peewee import SqliteDatabase, Model, CharField, DecimalField
db = SqliteDatabase('banco.db')
class Conta(Model):
titular = CharField()
saldo = DecimalField(decimal_places=2)
class Meta:
database = db
# Transação atômica básica
with db.atomic():
Conta.create(titular='Alice', saldo=1000.00)
Conta.create(titular='Bob', saldo=500.00)
 with db.atomic() as transacao_principal:
# Operação Principal
Conta.create(titular='Carlos', saldo=500.00)
try:
# Bloco aninhado: Peewee cria um Savepoint automaticamente
with db.atomic() as savepoint_secundario:
Conta.create(titular='Operação Riscada', saldo=-100.00)
raise ValueError("Erro simulado na sub-operação!")
except ValueError:
print("Sub-operação falhou! Rollback feito até o Savepoint.")
# A criação do 'Carlos' continua preservada e será comitada!
def transferir(id_origem, id_destino, valor):
try:
with db.atomic():
c_origem = Conta.get_by_id(id_origem)
c_destino = Conta.get_by_id(id_destino)
if c_origem.saldo < valor:
raise ValueError("Saldo insuficiente!")
# 1. Debita da conta de origem
c_origem.saldo -= valor
c_origem.save()
# Se ocorrer qualquer erro aqui, o débito acima será anulado
(Rollback)
# 2. Credita na conta de destino
c_destino.saldo += valor
c_destino.save()
print("Transferência realizada com sucesso!")
except Exception as e:
print(f"Erro na operação: {e}. O Rollback automático protegeu os dados.")