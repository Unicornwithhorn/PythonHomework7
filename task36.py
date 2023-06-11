# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
# operation = lambda x, y: x+ y

num_rows = num_columns = [i+1 for  i in range(int(input('Введите размер квадратно матрицы (по дефолту 6) ')))]
operation = eval('lambda x, y: ' + input('Введите функцию с аргументами x и y (например, x+y или х+ y*y) '))
def print_operation_table(operation, num_rows: list, num_columns: list):
    for i in num_rows:
        current_row_number = [i for x in num_rows]
        current_row = list(map(operation, num_columns, current_row_number))
        print(* current_row, sep='\t')

print_operation_table(operation, num_rows, num_columns)