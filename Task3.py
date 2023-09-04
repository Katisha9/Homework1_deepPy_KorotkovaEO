# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

lower_limit = 0
upper_limit = 1000
number_attempts = 10
counter = 0
num = randint(lower_limit, upper_limit)

while counter < number_attempts:
#    print (num)
    counter += 1
    entered_number = int(input("Введите число больше 0 и меньше 1000: "))

    if num == entered_number:
        print("Вы угадали!")
        break
    elif num > entered_number:
        print("Загаданное число больше")
        print(f"Осталось попыток {10 - counter}")
        upper_limit = num - 1
    else:
        print("Загаданное число меньше")
        print(f"Осталось попыток {10 - counter}")
        lower_limit = num + 1

else:
    print("Попытки исчерпаны")
    counter = -1


