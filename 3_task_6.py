import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')

printTimeStamp('Олександр Наживотов')

code = "9789609319614"

accum = 0
for item in range(0, len(code) - 1):
    if item % 2 != 0: 
        accum += int(code[item]) * 3
        
    else:
        accum += int(code[item]) * 1

result = 10 - (accum % 10)

print(accum)
print(result)
