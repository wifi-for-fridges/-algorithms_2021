"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def count_honest_digits_in_number(number, honest_count = 0, non_honest_count = 0):
    digit = number % 10
    new_number = number // 10

    if digit % 2 == 0:
        honest_count += 1
    else:
        non_honest_count += 1

    if new_number == 0:
        print(f'Количество четных и нечетных цифр в числе равно: ({honest_count}, {non_honest_count})')
        return
    count_honest_digits_in_number(new_number, honest_count, non_honest_count)


while True:
    try:
        number = int(input('Введите натуральное число: '))
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print('Вводить можно лишь натуральные числа и 0! Попробуйте еще раз.')

count_honest_digits_in_number(number)