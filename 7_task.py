first_num = int(input("Введите начальное число диапазона: "))
second_num = int(input("Введите конечное число диапазона: "))
num = int(input("Введите число: "))

deepen = range(first_num, second_num + 1)

while num not in deepen:
    print("Неверно, попробуйте еще раз.")
    num = int(input("Введите число: "))

print("Победа!")