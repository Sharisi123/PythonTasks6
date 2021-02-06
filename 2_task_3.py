import datetime


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')


printTimeStamp('Олександр Наживотов')

heigth = int(input('Enter your heigth '))

duim = heigth / 2.54
fute = 0
while duim > 12:
    duim -= 12
    fute += 1
    
print(f'Your height is {fute} fute and {round(duim)} duim')