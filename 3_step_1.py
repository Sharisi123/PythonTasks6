import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

i = 0
while True:
    i += 1
    line = input(f'Це циклiчний вивiд данний номер {i} \n')
    if line == 'end':
        break