'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:3}", end=" ")
            print()
        return " "

    def __add__(self, other):
        for a in range(len(self.my_list)):
            for b in range(len(other.my_list[a])):
                self.my_list[a][b] = self.my_list[a][b] + other.my_list[a][b]
        return Matrix.__str__(self)

matrix = Matrix(
    [
        [1, 2, 3],
        [-4, -5, -6],
        [7, 8, 9]
    ]
)
matrix1 = Matrix(
    [
        [10, 11, 12],
        [-13, -14, -15],
        [16, 17, 18]
    ]
)

print(matrix.__add__(matrix1))
