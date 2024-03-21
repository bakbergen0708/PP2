from datetime import date, timedelta

current_date = date.today()


yesterday = current_date - timedelta(days=1)
today = current_date
tomorrow = current_date - timedelta(days=1)

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

"""
import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
"""