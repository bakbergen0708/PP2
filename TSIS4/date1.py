from datetime import date, timedelta

current_date = date.today()

new_date = current_date - timedelta(days=5)

print(f"Current Date: {current_date}")
print(f"5 days before Current Date: {new_date}")

"""
from datetime import datetime, timedelta

current_time = datetime.now()

new_time = current_time - timedelta(hours=5)

new_time_str = new_time.strftime('%Y-%m-%d %H:%M:%S')

print(f"Current Time: {current_time}")
print(f"Time 5 hours ago: {new_time_str}")
"""
