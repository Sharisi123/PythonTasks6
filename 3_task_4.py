import datetime


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()) + '\n')


printTimeStamp('Олександр Наживотов')

result = 45
time = int(input('Time in network: '))
sms = int(input('SMS in network: '))
if time > 200:
   a = (time - 200) * 0.27
   result += a
if sms > 50:
    b = (sms - 50) * 0.5
    result += b

result_with_other = result + 1.44 + (result * 0.05)

print(f"Basic pay for using {round(result, 2)}")
print(f"With taxes {result_with_other}")