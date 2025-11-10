def seq1(n1,m1):
    yield 1
    for i in range(m1-1, n1*m1, m1-1):
        v1 = i % n1 + 1
        if v1 == 1: return
        yield v1


print("Введите n массива 1")
n1 = int(input())

print("Введите m массива 1")
m1 = int(input())

print(list(seq1(n1,m1)))

def seq2(n2,m2):
    yield 1
    for i in range(m2-1, n2*m2, m2-1):
        v2 = i % n2 + 1
        if v2 == 1: return
        yield v2


print("Введите n массива 2")
n2 = int(input())

print("Введите m массива 2")
m2 = int(input())

print(list(seq2(n2,m2)))
print("Общий путь:")
print(list(seq1(n1,m1)) + list(seq2(n2,m2)))