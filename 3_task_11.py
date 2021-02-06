import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

choice = int(input(""" Select the calc system:
    1 - 1 dog year = 7 human years
    2 - 2 first dog years = 10.5 human year, others = 4 human years
    Enter: """))
age = float(input('Enter your age: '))
a = 0
dog = 0
if age < 0:
    print('Error')

if choice == 1:
    dog = age / 7
else:
    while age >= 10.5:
        while dog != 2:
            age = age - 10.5
            dog += 1
    while age > 0:
        age = age - 4
        dog += 1
print(f'Your age in dog years is: {dog}')
