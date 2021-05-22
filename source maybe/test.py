import datetime

x = datetime.datetime.now()
"dd.MM.yyyy hh:mm:ss"
print(x.strftime("%d.%m.%Y %H:%M:%S"))