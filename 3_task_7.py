import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

count_of_water = int(input('Enter the quantity of water: '))
step = 1
accum = 20

while count_of_water > 0:
  if step == 1:
    if count_of_water >= 30:
        accum += count_of_water * 9.86
        count_of_water -= 30
        step += 1
  if step == 2:
    if count_of_water >= 20:
        accum += count_of_water * 11.22
        count_of_water -= 20
        step += 1
  if step == 3:
    if count_of_water >= 10:
        accum += count_of_water * 13.06
        count_of_water -= 10
        step += 1
  else:
    accum += count_of_water * 17.89

print(round(accum, 2))