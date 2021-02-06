import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

P = float(input('Input a pressue in Pa: '))
V = float(input('Input a volume in m^3: '))
T = float(input('Input a temperature in C*: '))
T += 273
R = 8.314
n = (P * V) / (R * T)
print(f'Molar mass of gas is {n}')