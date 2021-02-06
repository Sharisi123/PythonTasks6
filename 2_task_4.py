import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

dish_name = str(input('Enter the dish name: '))
dish_count = int(input('Enter the count of dish: '))
dish_price = int(input('Enter the price of dish: '))

order = dish_count * dish_price

tax = order * 0.18
tip = order * 0.14

result = order + tax + tip

print(f'The tax is {tax}')
print(f'The tips is {round(tip, 2)}')
print(f'All summ is {result}')