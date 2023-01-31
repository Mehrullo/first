import math
what = input("Что делаем? (+,-,*,/):")
y = float(input("Введите первое число: "))
x = float(input("Введите второе число: "))
if what == "-":
	c = y - x
	print("Результат: " + str(c))
elif what == "+":
	c = y + x
	print("Результат: " + str(c))
elif what == "*":
	c = y * x
	print("Результат: " + str(c))
elif what == "/":
	c = y / x
	print("Результат: " + str(c))
else:
	print("Выбрана неверная операция !")
input()

