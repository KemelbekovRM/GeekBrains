#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

param = input('Введите число: ')
param2 = param + param
param3 = param + param + param
summa_param = int(param) + int(param2) + int(param3)
print(f'Сумма чисел {param} + {param2} + {param3} = {summa_param}')

