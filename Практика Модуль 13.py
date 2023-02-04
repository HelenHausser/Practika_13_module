# получаем кол-во билетов
ticket = int(input("Введите кол-во билетов?: "))
# организуем цикл по билетам
i = 1
# итоговая сумма билетов
total_sum = 0
while i <= ticket:
    # запрос возраста для каждого билета
    age = int(input("Сколько вам лет?: "))
    if 18 <= age < 25:
        total_sum += 990
    elif age >= 25:
        total_sum += 1390
    i += 1
print("Общая сумма билетов: ",total_sum)
# считаем скидку
if ticket > 3:
    total_sum -= total_sum / 10
    print("Общая сумма билетов со скидкой 10%: ",total_sum)