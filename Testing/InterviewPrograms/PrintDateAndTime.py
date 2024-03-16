from datetime import date, timezone
from datetime import datetime
import pytz

today = date.today()
print("Today's Date: ", today)

print("****************************")
#dd/mm/yy
df1 = today.strftime("%d/%m/%y")
print(df1)
df2 = today.strftime("%d/%b/%y")
print(df2)
df3 = today.strftime("%d%B%Y")
print(df3)
print("*********************************")
timeAndDate = datetime.now()
currentDateANdTime = timeAndDate.strftime("%d/%b/%y %H:%M:%S")
print(currentDateANdTime)

timeAndDateZone = pytz.timezone('America/New_York')
newyorkTime = datetime.now(timeAndDateZone)
print(newyorkTime)

timeAndDateZoneIndia = pytz.timezone('Asia/Calcutta')
indiaTime = datetime.now(timeAndDateZoneIndia)
print(indiaTime)

print("****************************************")
utcTime = datetime.utcnow()
print(utcTime)

date_time = datetime.now()
print(date_time.utcoffset())