

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



# print(circle1.circumference)
# print(circle2.circumference)

# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).
#
# Решение:






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