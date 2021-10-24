import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
today = datetime.date.today()
print(today)
print(today.isoformat())
d = datetime.timedelta(weeks=-1)
print(d)
print(now-d)
