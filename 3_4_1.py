'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется
ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится,
надо отправить в качестве ответа на эту задачу.

Sample Input:     a3b4c2e10b1
Sample Output:    aaabbbbcceeeeeeeeeeb

обратная задача 2_4_2
'''

import re                                           # импорт модуля для работы с регулярными выражениями
numbs, chairs = [], []
result_str = ''

with open('dataset_3363_2.txt', 'r') as inputData:  # открываем файл
    str = inputData.readline().strip()              # считываем строку данных из файла в переменную
    print(str)                                      # выводиим на экран, контроль считывания.
    # Файл закрыт

    numbs = re.findall(r'\d+', str)                 # выбираем все числовые значения из строки
    chairs = re.findall(r'\D', str)                 # выбираем все НЕчисловые значения из строки
    for i in range(0, len(numbs)):                  # перемножаем
        result_str += chairs[i] * int(numbs[i])
    print(result_str)

with open('dataset_3363_2_output.txt', 'w') as outputData:   # открываем файл на запись
    outputData.write(result_str)                    # записываем результат в файл
    # файл закрыт