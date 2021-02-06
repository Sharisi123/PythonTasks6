import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

num = input('Input a number: ')
accum = 0
for i in range(0, len(num)):
    accum += int(num[i])

print(f'The sum of digits is: {accum}')