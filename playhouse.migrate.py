from playhouse.migrate import SqliteMigrator, migrate
migrator = SqliteMigrator(db)
status_field = CharField(default='Ativa', null=False)
# Executa o ALTER TABLE sem apagar os registros da tabela
migrate(
migrator.add_column('conta', 'status', status_field)
)