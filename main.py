import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Олександр Наживотов')

name = 'Iванов Iван Iванович'
age = '47'
print(f'\nМене звати {name}, менi {age}')