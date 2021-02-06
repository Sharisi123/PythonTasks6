import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

char = str(input('Enter a char: '))

if char == "a" or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print('it\'s a loud char')
elif char == 'y':
    print('it\'s a loud char and unloud at one time, depends situation')
else:
    print('it\'s a unloud char')