import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

celcius = float(input('Enter the temperature i Celcius: '))
kelvin = celcius + 273.15
farengeit = (celcius * 9/5) + 32
print(f"In Kelvin: {kelvin}")
print(f"In Farengeit: {farengeit}")