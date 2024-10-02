import time
import datetime


time_seconds = (time.time())
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {time_seconds:.4f} or {time_seconds:.2e} in scientific notation")
print(formatted_time)