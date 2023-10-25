first_num = int(input("Введите начальное число диапазона: "))
second_num = int(input("Введите конечное число диапазона: "))

deepen = range(first_num, second_num + 1)
sum = sum(deepen)

print("Сумма диапазона:", sum)
