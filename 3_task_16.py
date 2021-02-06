import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

a = []
b = None
accum = 0
while b != '':
    b = input('Enter a groop: ')
    a.append(b)

a.remove('')

for i in range(0, len(a)):
    if int(a[i]) < 3:
        accum += 0
    elif int(a[i]) >= 3 and int(a[i]) <= 12:
        accum += 16
    elif int(a[i]) > 60:
        accum += 18
    else:
        accum += 25

if len(a) > 9:
    accum -= (accum * 0.1)

print(f'group length is {len(a)}')
print(f'The tickets cost is: {accum}')