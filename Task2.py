# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


a = int(input("Введите число от 0 до 100000 включительно: "))
while not 0 < a < 100001:
    a = int(input("Введите число от 0 до до 100000 включительно: "))
if a == 1 or a == 0:
    print("Число не является ни простым, ни составным.")

k = 0
for i in range(2, a):
    if (a% i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число составное")