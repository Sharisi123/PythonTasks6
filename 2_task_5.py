import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

a = int(input('How many shtychki you need? '))
b = int(input('How many shtycensii you need? '))

SHTYCKA = 75
SHTYKENCIA = 112
i = 1
j = 1

while i < a:
    SHTYCKA += SHTYCKA
    i += 1

while j < b:
    SHTYKENCIA += SHTYKENCIA
    j += 1

result = SHTYCKA + SHTYKENCIA

print(result)