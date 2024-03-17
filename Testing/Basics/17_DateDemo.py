
#current date and time
import datetime
now = datetime.datetime.now()
print("Current date and time :")
print(now.strftime("%Y%m%d_%H%M%S"))

print("**********************************************************")
#  after 4 days date from the current date
from datetime import datetime,timedelta
current_date = datetime.now().date()
future_date =current_date + timedelta(days=4)
print("Current date :",current_date)
print("future Date 4 days from now :",future_date)

print("**********************************************************")
# before 4 days  date from the current date
from datetime import datetime,timedelta
current_date = datetime.now().date()
past_date =current_date - timedelta(days=4)
print("Current date :",current_date)
print("Date 4 days back from now :",past_date)