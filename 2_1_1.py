'''
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.

Sample Input 1: 5 -3 8 4 0
Sample Output 1:  14
'''

summa = 0
i = int( input())
if i != 0:
    while i != 0:
        summa += i
        i = int( input())
        if i == 0:
            print(summa)
else:
    print(summa)