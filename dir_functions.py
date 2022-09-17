import platform
import datetime

x = dir(platform)
# print(x)
y = datetime.datetime.now()
print(y.day)
print(y.month)
print(y.year)
print(y.strftime("%A"))

