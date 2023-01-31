import math
from prettytable import PrettyTable
num = 120
numerator = 1-num
value = []
answer = []
while True:
    try:
        start_diapason = int(input("Введите начальное значение диапазона :"))
        end_diapason = int(input("Введите второе значение диапазона :"))
        step_diapason = int(input("Введите шаг диапазона :"))
        break
    except ValueError:
        print("Введите числа.")
for x in range(start_diapason, end_diapason, step_diapason):
    value.append(x)
    cos=math.degrees(math.cos(x))
    sin_num = math.degrees(math.sin(x + num))
    division_sin = numerator/sin_num
    if cos == 0:
        answer.append("значение cos или sin равен 0")
    elif num == 0:
        answer.append("деление на ноль")
    elif division_sin <= 0:
        answer.append("логарифм из отрицательного числа")
    else:
        even_numbers = math.log(division_sin, 21), abs(cos/num)
        answer.append(max(even_numbers))
mytable = PrettyTable()
mytable.add_column("значение x", value)
mytable.add_column("ответ", answer)
print(mytable)
input()