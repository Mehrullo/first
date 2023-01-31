from random import randint

def buble_sort(arr):
    count_if = 0
    count_move = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            count_if += 1
            if arr[j] > arr[j + 1]:
                count_move += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, count_if, count_move
def insertion_sort(arr):
  count_if = 0
  count_move = 0

  for i in range(1, len(arr)): 
 
    value = arr[i]
    j = i - 1 
    count_if += 1
    while j >= 0 and value < arr[j]: 
      arr[j + 1] = arr[j] 
      j -= 1 
    arr[j + 1] = value
    count_move += 1 
  return arr, count_if, count_move 
n_arr=[51,103,207,418,849,1725,3513]
for n in n_arr:
  n_arr=[]
  for i in range(n):
    n_arr.append(randint(-100, 100))

  print("Исходный массив ", n_arr)
  print("======Количество символов====== ", n)
  n_arr, count_if, count_move = buble_sort(n_arr)
  print("Пузырьковая сортировка", n_arr)
  print(f"Количество сравнений: {count_if} " f"Количество перестановок: {count_move}")
  n_arr, count_if, count_move = insertion_sort(n_arr)
  print("Cортировка вставками", n_arr)
  print(f"Количество сравнений: {count_if} " f"Количество перестановок: {count_move}")
print("Конец")

