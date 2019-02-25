import math

while True:
    number = (input("Write time in minutes, use 'q' for exit:"))
    if number == 'q':
        break
    elif not number.isnumeric():
        print("Error, don't use letters and signs!")
    else:
        number = int(number)
        minutes = number % 60
        number = math.floor(number / 60)  # here are only hours

        hours = math.floor(number % 24)
        number = math.floor(number / 24)  # here are only days

        days = math.floor(number % 30)
        number = math.floor(number / 30)  # here are only months

        print('{} months {} days {} hours {} minutes'.format(number, days, hours, minutes))
        break
