
import math

number = (input('Time in minutes:'))

if not number.isnumeric():
    print("Error, don't use letters and signs")
else:
    hour = math.floor(int(number)/60)
    minutes = int(number)%60

    print('{}h {}m'.format(hour, minutes))
    
