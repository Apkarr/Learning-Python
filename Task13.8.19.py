tickets = int(input("Укажите необходимое количество билетов:"))
price = 0.0
for i in range(1, tickets + 1):
    age = int(input('Укажите возраст: '))
    if age >= 25:
        price = price + 1390
    elif 18 <= age < 25:
        price = price + 990
    else:
        price = price + 0

if tickets <= 3:
    pass
else:
    price= price * 0.9
    print('Поздравляем, у вас скидка 10%')
print('Общая стоимость билетов:'+' ' + str(round(price)) + ' ' + 'рублей')
