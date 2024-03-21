from datetime import datetime

date1 = datetime(2024, 3, 9, 12, 50, 0)  
date2 = datetime.now()  

time_difference = date2 - date1

seconds_difference = time_difference.total_seconds()

print(f"{int(seconds_difference)} seconds")
