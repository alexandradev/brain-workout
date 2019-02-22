
import math

while True:
        number = (input("Write time in minutes, use 'q' for exit:"))
        if number == 'q':
            break
        elif not number.isnumeric():
            print("Error, don't use letters and signs!")
        else:
            hour = math.floor(int(number)/60)
            minutes = int(number)%60

            print('{}h {}m'.format(hour, minutes))
            break
