import time

hourly_rate = float(input('Please input your hour rate: '))
total = 0

while True:
  total += hourly_rate / 60 / 60
  print(round(total, 2))
  time.sleep(1)
