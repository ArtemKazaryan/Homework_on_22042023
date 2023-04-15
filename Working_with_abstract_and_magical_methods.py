

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!


# Домашняя работа на 22.04.2023.


# Модуль 10. Объектно-ориентированное
# программирование
#
# Тема: Статические методы

# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).
#
# Решение:
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.circumference = round(2 * pi * self.radius, 3)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.circumference > other.circumference
    def __lt__(self, other):
        return self.circumference < other.circumference
    def __ge__(self, other):
        return self.circumference >= other.circumference
    def __le__(self, other):
        return self.circumference <= other.circumference

    def __add__(self, other):
        return round(2 * pi *(self.radius + other), 3)
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        self.radius += other
        return round(2 * pi * self.radius, 3)

    def __sub__(self, other):
        return round(2 * pi * (self.radius - other), 3)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __isub__(self, other):
        self.radius -= other
        return round(2 * pi * self.radius, 3)

circle1 = Circle(1)
circle2 = Circle(2)
circle3 = Circle(1)

print()
print('Проверка на равенство радиусов двух окружностей:')
print(circle1 == circle2)
print(circle1 == circle3)

print()
print('Сравнения длин двух окружностей:')
print(circle1 > circle2)
print(circle2 > circle1)
print(circle1 >= circle2)
print(circle2 >= circle1)

print()
print('Пропорциональное изменение размеров окружности, путём изменения ее радиуса:')
summ = circle1 + 1
print(summ)
subs = circle2 - 1
print(subs)
circle1 += 1
print(circle1)
circle2 -= 1
print(circle2)


# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций по работе с комплексными
# числами (операции +, -, *, /).
#
# Решение:

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        print(f'{self.real + other.real} + ({self.imaginary + other.imaginary}) * i')
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)
    def __radd__(self, other):
        return

    def __sub__(self, other):
        print(f'{self.real - other.real} + ({self.imaginary - other.imaginary}) * i')
        return Complex(self.real - other.real,
                       self.imaginary - other.imaginary)
    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        print(f'{self.real * other.real - self.imaginary * other.imaginary}'
              f' + ({self.real * other.imaginary + self.imaginary * other.real}) * i')
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        print(f'{(self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)}'
              f' + ({(self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)}) * i')
        return Complex((self.real * other.real + self.imaginary * other.imaginary) /
                       (other.real ** 2 + other.imaginary ** 2),
                       (self.imaginary * other.real - self.real * other.imaginary) /
                       (other.real ** 2 + other.imaginary ** 2))

# для простоты возьмём комплексно-сопряжённые числа
complex_num1 = Complex(1, 1)
complex_num2 = Complex(1, -1)

print()
print('Результат сложения двух комплексных чисел (2 способа вывода):')
complex_num3 = complex_num1 + complex_num2
# либо
print(f'{complex_num3.real} + ({complex_num3.imaginary}) * i')

print()
print('Результат вычитания двух комплексных чисел (2 способа вывода):')
complex_num3 = complex_num1 - complex_num2
# либо
print(f'{complex_num3.real} + ({complex_num3.imaginary}) * i')

print()
print('Результат умножения двух комплексных чисел (2 способа вывода):')
complex_num3 = complex_num1 * complex_num2
# либо
print(f'{complex_num3.real} + ({complex_num3.imaginary}) * i')

print()
print('Результат деления двух комплексных чисел (2 способа вывода):')
complex_num3 = complex_num1 / complex_num2
# либо
print(f'{complex_num3.real} + ({complex_num3.imaginary}) * i')



# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# 1
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).
#
# Решение:





# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).
#
# Решение: