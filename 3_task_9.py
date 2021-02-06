import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

db = int(input('Input the noise in db: '))

if db < 40:
    print('This noise is quiter then quite room')
elif db == 40:
    print('This noise is like quite room')
elif db > 40 and db < 70 :
    print('This noise is between quite room and alarm clock')
elif db == 70:
    print('This noise is like alarm clock')
elif db > 70 and db < 106:
    print('This noise is between alarm clock and petrol lawn mower')
elif db == 106:
    print('This noise is like petrol lawn mower')
elif db > 106 and db < 130:
    print('This noise is between petrol lawn mower and jackhammer')
elif db == 130:
    print('This noise is like jackhammer')
elif db > 130:
    print('This noise is louder than jackhammer')
else:
    print('Error')
