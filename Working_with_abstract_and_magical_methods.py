

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
print(circle1 < circle2)
print(circle1 >= circle3)
print(circle2 <= circle1)

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


# Решение:

class Airplane:
    def __init__(self, airplane_type, pass_num, pass_capacity):
        self.airplane_type = airplane_type
        self.pass_num = pass_num
        self.pass_capacity = pass_capacity

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __add__(self, other):
        if self.pass_num + other <= 0:
            return 0
        if self.pass_num + other <= self.pass_capacity:
            return self.pass_num + other
        else:
            print()
            print('Количество пассажиров не может быть больше вместимости!!! Изменения не выполнены!!!')
            return self.pass_num
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        self.pass_num += other
        if self.pass_num <= 0:
            return 0
        if self.pass_num <= self.pass_capacity:
            return self.pass_num
        else:
            print()
            print('Количество пассажиров не может быть больше вместимости!!! Изменения не выполнены!!!')
            self.pass_num -= other
            return self.pass_num

    def __sub__(self, other):
        if self.pass_num - other <= 0:
            return 0
        else:
            return self.pass_num
    def __rsub__(self, other):
        return self.__sub__(other)
    def __isub__(self, other):
        self.pass_num -= other
        if self.pass_num <= 0:
            return 0
        else:
            return self.pass_num

    def __gt__(self, other):
        return self.pass_capacity > other
    def __lt__(self, other):
        return self.pass_capacity < other
    def __ge__(self, other):
        return self.pass_capacity >= other
    def __le__(self, other):
        return self.pass_capacity <= other

airplane1 = Airplane('Военный', 10, 15)
airplane2 = Airplane('Гражданский', 100, 200)
airplane3 = Airplane('Гражданский', 50, 200)

print()
print('Проверка на равенство типов самолетов:')
print(airplane1 == airplane2)
print(airplane2 == airplane3)

print()
print('Увеличение и уменьшение пассажиров в салоне самолета:')
summ = airplane1 + 2
print(summ)
subs = airplane2 - 5
print(subs)
airplane2 += 4
print(airplane2)
airplane3 -= 5
print(airplane3)

print()
print('Сравнение двух самолетов по максимально возможному количеству пассажиров на борту:')
print(airplane1 > airplane2)
print(airplane1 < airplane2)
print(airplane2 >= airplane3)
print(airplane1 <= airplane3)





# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).
#
# Решение: