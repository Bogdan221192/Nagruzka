a = input('введите путь к файлу')
b = open(a, 'r').read()
c = [int(x) for x in b.split()]
print(c)

from statistics import median
m = median(c)
moves = (sum(abs(v - m) for v in c))
if moves > 20:
    print ("Невозможно сделать за 20 ходов")
else:
    print ('Возможно привести за количество ходов:')
    print (moves)