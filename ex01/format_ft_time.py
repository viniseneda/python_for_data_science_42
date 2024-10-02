import time
import datetime
from decimal import Decimal


time_seconds = (time.time())
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%b %d %Y")

time_scientific = '%.2E' % Decimal(time.time())
print (f"Seconds since January 1, 1970: {time_seconds} or {time_scientific} in scientific notation")


current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%b %d %Y")
print(formatted_time)