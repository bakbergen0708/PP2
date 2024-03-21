from datetime import datetime, timedelta

current_datetime = datetime.now()

new_datetime = current_datetime.replace(microsecond=0)

print("Current Datetime:", current_datetime)
print("Datetime without Microseconds:", new_datetime)
