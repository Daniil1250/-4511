# ___ = int(input("Введите число N: "))

# summ = 0

# ___ num ___ range(1, N + 1):
#     ___ num % 2 ___ 0:
#         summ ___ summ + num

# print(f"Сумма всех чётных чисел от 1 до {N} = ___")

# import math

# print(math.sqrt(16))

# print(math.factorial(5))

# print(math.sin(math.pi / 2))
# print(math.pi)

# print(math.pow(2, 3))



# import random as r

# print(r.randint(1, 10))

# fruits = ["яблоко", "банан", "вишня"]
# print(r.choice(fruits))

# r.shuffle(fruits)
# print(fruits)


# from math import sqrt, pow
# from random import randint

# print(sqrt(64), "\n", pow(3, 2), "\n", randint(1, 100))



# import turtle as t

# t.shape("turtle")
# t.color("red")
# t.speed(5)

# t.forward(30)
# t.left(90)
# t.forward(30)
# t.left(90)
# t.forward(30)
# t.left(90)
# t.forward(30)

# t.done()



# import turtle as t

# from turtle import *

# shape("turtle")
# color("blue")
# speed(3)

# for i in range(4):
#   forward(30)
#   left(90)

# done()


# from turtle import *

# shape("turtle")
# color("black")
# speed(2)

# circle(50)

# done()



# from turtle import *

# shape("turtle")
# color("black")
# speed(2)

# for i in range(5):
#   left(90)
#   forward(50)

# left(45)
# forward(50)
# left(45)
# forward(50)

# done()

# функции - круглые скобки
# массив, список - квадратные скобки

# nested = [[1, 2], [3, 4], "apple"]

# print(nested[0])
# print(nested)
# print(nested[-1])


# fruits = ["банан", "виноград"]

# print(fruits)

# fruits.append("груша") # добавления элемента, в конец списка
# print(fruits)
# print("="*40)

# fruits.insert(1, "вишня") # добавления элемента по индексу
# print(fruits)
# print("="*40)

# fruits.remove("банан") # удаляю ВЫБРАНЫЙ элемент из списка
# print(fruits)
# print("="*40)

# fruits.pop() # удаляю ПОСЛЕДНИЙ элемент из списка
# print(fruits)
# print("="*40)

# print("Длинна списка: ", len(fruits))


# numbers = [3, 1, 4, 2]
# numbers.sort() # сортировка по возрастанию
# print(numbers)

# numbers.reverse() # записываю элементы справа -> налево
# print(numbers)


fruits = ["банан", "виноград", "вишня"]

for fruit in fruits: # перебор списка, прохожусь по каждому элементу
  print(fruit)

for i in range(len(fruits)):
  print(f"Элемент {i}: {fruits[i]}")
