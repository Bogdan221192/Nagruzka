import sys

a = sys.argv[1]
b = open(a, 'r').read()
c = [int(x) for x in b.split()]
numbers = []
for item in c:
    try:
        # Поддерживаем целые и дробные числа
        num = float(item)
        # Если число целое (например, 5.0), преобразуем в int
        if num.is_integer():
            numbers.append(int(num))
        else:
            print(f"Предупреждение: число '{item}' не целое, будет проигнорировано.")
    except ValueError:
        print(f"Предупреждение: '{item}' не является числом, будет проигнорировано.")

    # Проверка, что нашлись хотя бы одни целые числа
if not numbers:
    print("Ошибка: в файле не найдено ни одного целого числа.")

print(c)

from statistics import median
m = median(c)
moves = (sum(abs(v - m) for v in c))
if moves > 20:
    print ("Невозможно сделать за 20 ходов")
else:
    print ('Возможно привести за количество ходов:')
    print (moves)