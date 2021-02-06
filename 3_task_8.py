import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

cost = float(input('Input the coffee cost: '))
money = float(input('Input your money: '))

if money < cost:
    print('Not enough money')
else:
    money -= cost

a = 0
b = 0
c = 0
d = 0

while money > 0:
    if money >= 5:
        money -= 5
        a += 1
    if money >= 2:
        money -= 2
        b += 1
    if money >= 1:
        money -= 1
        c += 1
    if money >= 0.5:
        money -= 0.5

print(f'Your fragmented change is {a} in 5$, {b} in 2$, {c} in 1$ and {d} in 0.5$ ')