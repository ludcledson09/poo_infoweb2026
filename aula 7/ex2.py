import datetime
from zoneinfo import ZoneInfo

x = datetime.datetime(2026, 5, 1)
print(x)
print(type(x))

y = datetime.datetime(2026, 5, 19, 14, 30, 0)
print(y)
print(y.day)
print(y.month)
print(y.year)
print(y.hour)
print(y.minute)
print(y.second)
print(y.date())
print(y.time())
print(y.weekday())

#from zoneinfo import ZoneInfo
#z=datetime.datetime.now(ZoneInfo("America/Sao_Paulo"))
z=datetime.datetime.now()
print(z)
print(z.strftime("%d/%m/%Y, %h:%m:%s"))
print(z.strftime("%d/%m/%Y"))
print(z.strftime("%d/%m/%Y, %a"))
print(z.strftime("%d/%m/%Y, %A %B"))
