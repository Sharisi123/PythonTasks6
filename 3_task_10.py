import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

print("""Choose the measure system:  
    1 - height in inch, weigth in foot
    2 - height in meter, weigth in kilogram""")
a = int(input('Answer: '))
heigth = float(input('Enter your heigth: '))
weigth = float(input('Enter your weigth: '))

if a == 1:
    result = 703 * (weigth/(heigth ** 2))
else:
    result = weigth / (heigth ** 2)

print(f'your body mass index is {round(result, 2)}')
