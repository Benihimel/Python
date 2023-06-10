# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Specify the number of elements in the array: "))
A = []
i = 1
while i <= N:
    A.append(i)
    i += 1

print(f"Array: {A}")
X = int(input("Enter number: "))
number = 0
for i in range(len(A)):
    if ((X - A[i]) < X - number) and (X - A[i]) > 0:
        number = i
print(f"Number {X} closest to the value in the array: {A[number]}")


