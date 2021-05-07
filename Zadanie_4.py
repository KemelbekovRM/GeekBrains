# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

param = int(input('Введите число - '))
itog = 0
while param > 0:
    max_chislo = param % 10
    param //= 10
    if max_chislo > itog:
        itog = max_chislo
print(itog)

