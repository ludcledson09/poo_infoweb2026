from datetime import datetime

class Service:
 def horario_abrir_agenda(data, inicio, fim, intervalo,
  id_profisional):
  dt = datetime.strptime(data, "%d/%m/%Y")
  if dt.date() < datetime.now().date():
    raise ValueError("Data não pode estar no passado")
  if intervalo > 120:
    raise ValueError("Intervalo máximo é 120 min")