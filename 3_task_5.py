import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

c = 4.186
m = float(input('Enter an m: '))
T = float(input('Enter an delta T: '))

q = m * c * T

P = q/ (1000 * 360)

cost = P * 1.33

print(round(cost, 4))