# Напишите программу, которая считывает список чисел lst из первой строки и число
# x из второй строки, которая выводит все позиции, на которых встречается число x
# в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку
# "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

lst, number = [int(i) for i in input().split()], int(input())
if lst.count(number) != 0:
    for i in range(len(lst)):
        if lst[i] == number: print(i, end=' ')
else: print('Отсутствует')