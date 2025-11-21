import sys

def parse_args():
    """Парсинг и валидация аргументов командной строки."""
    if len(sys.argv) != 5:
        print("Ошибка: требуется ровно 4 аргумента — n1 m1 n2 m2.")
        print("Пример: python script.py 5 3 4 2")
        sys.exit(1)

    try:
        n1 = int(sys.argv[1])
        m1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        m2 = int(sys.argv[4])
    except ValueError:
        print("Ошибка: все аргументы должны быть целыми числами.")
        sys.exit(1)

    # Проверка на положительность
    if n1 <= 0 or m1 <= 0 or n2 <= 0 or m2 <= 0:
        print("Ошибка: все параметры (n1, m1, n2, m2) должны быть > 0.")
        sys.exit(1)

    return n1, m1, n2, m2

def generate_sequence(n, m):
    """Генерирует последовательность по правилам задачи."""
    result = []
    i = 1

    while True:
        result.append(i)
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

    return result

def main():
    # Получаем и проверяем аргументы
    n1, m1, n2, m2 = parse_args()

    # Генерируем последовательности
    result1 = generate_sequence(n1, m1)
    result2 = generate_sequence(n2, m2)

    # Выводим результаты
    print(result1)
    print(result2)
    print("Общий путь:")
    print(result1 + result2)



main()