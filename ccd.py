import os
from peewee import SqliteDatabase, Model, CharField, DecimalField, IntegerField
from playhouse.migrate import SqliteMigrator, migrate
# 1. Configuração Inicial do Banco de Dados
DB_NAME = 'sistema_bancario.db'
if os.path.exists(DB_NAME):
os.remove(DB_NAME)
db = SqliteDatabase(DB_NAME)
class ContaBancaria(Model):
titular = CharField()
saldo = DecimalField(decimal_places=2, max_digits=10)
class Meta:
database = db
db.connect()
db.create_tables([ContaBancaria])
# 2. Inserção de Dados Iniciais
ContaBancaria.create(titular="Alice", saldo=1000.00)
ContaBancaria.create(titular="Bob", saldo=300.00)
def exibir_saldos(titulo):
print(f"\n--- {titulo} ---")
for conta in ContaBancaria.select():
print(f"ID {conta.id} | Titular: {conta.titular} | Saldo: R$
{conta.saldo:.2f}")
exibir_saldos("Saldos Iniciais")
# 3. Função de Transferência com Simulação de Falha (Rollback Total)
def transferir_valores(id_origem, id_destino, valor, simular_erro=False):
print(f"\n>> Tentando transferir R$ {valor:.2f} da Conta {id_origem} para
Conta {id_destino}...")
try:
with db.atomic():
c_origem = ContaBancaria.get_by_id(id_origem)
c_destino = ContaBancaria.get_by_id(id_destino)
if c_origem.saldo < valor:
raise ValueError("Saldo insuficiente!")
# Etapa 1: Debita da origem
c_origem.saldo -= valor
c_origem.save()
# Simulação de erro de sistema/rede
if simular_erro:
raise RuntimeError("FALHA DE CONEXÃO/SISTEMA NO MEIO DA
TRANSAÇÃO")
# Etapa 2: Credita no destino
c_destino.saldo += valor
c_destino.save()
print("Transferência concluída com SUCESSO!")
except Exception as e:
print(f"ERRO NA OPERAÇÃO: {e}")
print("ROLLBACK EXECUTADO! O saldo da conta de origem foi restaurado.")
# Teste 1: Transferência com Sucesso
transferir_valores(id_origem=1, id_destino=2, valor=200.00, simular_erro=False)
exibir_saldos("Saldos Após Transferência Com Sucesso")
# Teste 2: Transferência Com Erro (Demonstração de Rollback)
transferir_valores(id_origem=1, id_destino=2, valor=500.00, simular_erro=True)
exibir_saldos("Saldos Após Erro na Transferência (Valores Intactos)")
# 4. Demonstração Prática de Savepoint (Transação Aninhada)
print("\n" + "="*50)
print("DEMONSTRAÇÃO DE SAVEPOINT (db.atomic() Aninhado)")
print("="*50)
try:
with db.atomic() as transacao_pai:
# Cria uma conta válida na transação principal
ContaBancaria.create(titular="Charlie", saldo=1500.00)
print("Charlie criado na transação principal.")
try:
# Savepoint automático criado pelo bloco aninhado
with db.atomic() as savepoint_filho:
ContaBancaria.create(titular="Conta Com Erro", saldo=0.00)
print(">> Tentando executar sub-operação com erro...")
raise ValueError("Erro proposital na sub-operação")
except ValueError as sub_erro:
print(f"Erro capturado no Savepoint: {sub_erro}")
print("Sub-operação revertida para o Savepoint. A transação principal
continua!")
# Outra operação válida na transação principal
ContaBancaria.create(titular="David", saldo=800.00)
print("David criado na transação principal.")
except Exception as e:
print(f"Erro geral: {e}")
exibir_saldos("Saldos Após Demonstração de Savepoints (Charlie e David salvos,
Conta Com Erro descartada)")
# 5. Demonstração de Migração de Banco de Dados
print("\n" + "="*50)
print("INICIANDO MIGRAÇÃO DE ESQUEMA (playhouse.migrate)")
print("="*50)
migrator = SqliteMigrator(db)
# Novos campos para a tabela existente
status_field = CharField(default='Ativa', null=False)
limite_field = IntegerField(default=1000)
# Execução da alteração da tabela
migrate(
migrator.add_column('contabancaria', 'status', status_field),
migrator.add_column('contabancaria', 'limite_credito', limite_field)
)
print("Novas colunas adicionadas com sucesso sem apagar os dados antigos")
# Verificação dos dados após a migração
cursor = db.execute_sql("SELECT id, titular, saldo, status, limite_credito FROM
contabancaria;")
print("\n--- Tabela Final Pós-Migração ---")
for row in cursor.fetchall():
print(f"ID: {row[0]} | Titular: {row[1]} | Saldo: R${row[2]:.2f} | Status:
{row[3]} | Limite: R${row[4]}")
db.close()