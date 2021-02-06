import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

home = str(input('Where are you live? '))
time = int(input('How much time you are at home? '))

print('Вам слiд вибрати: ')
if home == 'Будинок':
    if time > 18: 
        print('В\'этнамське порося')
    if time > 10 & time < 17: 
        print('Собака')
    if time < 10: 
        print('Змiя')

if home == 'Квартира':
    if time < 10: 
        print('Кiшка')
    if time > 10: 
        print('Хом\'як')

if home == 'Гуртожиток':
    if time > 6: 
        print('Рибки')
    if time < 6: 
        print('Мурашник')