import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0)
    return math.sqrt(number)

number = 25100
delay_ms = 2123
result = delayed_square_root(number, delay_ms)

print(f"Квадратный корень из {number} после {delay_ms} миллисекунд равен {result}")
