import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

bread = 8.50

count_of_bread = float(input('How many bread you will buy? '))
bread_cost = bread * count_of_bread
discount = bread_cost * 0.6
result = bread_cost - discount
print(f'Normal cost of bread is {bread_cost}')
print(f'Discount is {discount}')
print(f'Result cost of bread is {round(result, 2)}')