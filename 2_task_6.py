import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

days = int(input('Enter days: '))
hours = int(input('Enter hours: '))
minutes = int(input('Enter minutes: '))
seconds = int(input('Enter seconds: '))

result = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
print(f'The result is: {result}')