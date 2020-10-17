# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime

datetimeString = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print('Current date and time :')
print(datetimeString)
