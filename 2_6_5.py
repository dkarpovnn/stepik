# Выведите таблицу размером n×n, заполненную числами от 1 до n*n по спирали, выходящей из левого верхнего угла
# и закрученной по часовой стрелке, как показано в примере (здесь n=5):

# Sample Input:
# 5

# Sample Output:
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]       # создаю матрицу n*n и заполняю нулями
k = 1                                               # заполняю матрицу числом к увеличивая его на 1 после заполнения каждого элемента
m = 0                                               # счётчик итераций спирали, увеличиваю на 1 на каждом витке спирали
while k <= n*n:                                     # внешний цикл с 4 вложенными циклами пока k не заполнит всю матрицу n*n
    for i in range(m, n-m):                         # цикл заполняет верхнюю сторону спирали - на каждой итерации сужаем границы
        a[m][i]= k                                  # цикла на m с каждой стороны
        k += 1
    for i in range(m+1, n-m):                       # цикл заполняет правую сторону спирали, границы зависят от m
        a[i][n-m-1]= k
        k += 1
    for i in range(n-m-2, m-1, -1):                 # заполняею нижнюю сторону спирали - зависит от m
        a[n-m-1][i] = k
        k += 1
    for i in range(n-2-m,m, -1):                    # цикл заполняет леаую сторону спирали - зависит от m
        a[i][m] = k
        k += 1
    m += 1
for i in range(n):                                  # вывод на печать каждого элемента матрицы
    for j in range(n):
        print(a[i][j], end ='\t')
    print()