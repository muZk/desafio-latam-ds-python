import sys

year = int(sys.argv[1])

if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
    print("El año {} es un año bisiesto".format(year))
