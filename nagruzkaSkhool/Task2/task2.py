import sys
from decimal import *
getcontext().prec = 40       # Set a new precision, возьмем с запасом, больше 38
# Чтение данных из файла
f1 = sys.argv[1]  # Файл с параметрами эллипса
f2 = sys.argv[2]  # Файл с координатами точек

try:
    with open(f1, "r") as file:
        line1 = file.readline().split()
        c = float(line1[0])
        d = float(line1[1])

        line2 = file.readline().split()
        a = float(line2[0])
        b = float(line2[1])
except FileNotFoundError:
    print("Файл не найден.")
    exit()

def calculate_point_position(c, d, a, b, x, y):
    if a == 0 or b == 0:
        return "Ошибка: полуоси не могут быть равны нулю."

    # Уравнение эллипса
    result = ((x - c)**2 / a**2) + ((y - d)**2 / b**2)

    if result < 1:
        return "1 - точка внутри"
    elif result == 1:
        return "0 - точка лежит на окружности"
    else:
        return "2 - точка снаружи."
points = []
try:
    with open(f2, 'r') as f:
        for line in f:
            try:
                    x, y = map(float, line.split())
                    points.append((x, y))
            except (ValueError, IndexError):
                    print(f"Предупреждение: неверный формат строки в файле '{f2}': '{line.strip()}'. Строка пропущена.")

except FileNotFoundError:
        print(f"Ошибка: файл '{f2}' не найден.")
if not (1 <= len(points) <= 100):
    print("Предупреждение: количество точек должно быть от 1 до 100.")

print(f"Центр эллипса: ({c}, {d})")
print(f"Полуоси: a={a}, b={b}")
print("-" * 20)

for x, y in points:
    position = calculate_point_position(c, d, a, b, x, y)
    print(f"Точка ({x}, {y}): {position}")