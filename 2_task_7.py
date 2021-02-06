import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

balance = 0
p = float(input('Початковий внесок: '))
r = float(input('Рiчна номiнальна ставка: '))
t = float(input('Кiлькiсть рокiв: '))
n = 1

result = p * (1 + r/n)**(t*n)

balance += result
print(round(balance, 2))