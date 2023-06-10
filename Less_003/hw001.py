# Задача 16: Требуется вычислить, сколько раз встречается
# некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1


N = int(input("Specify the number of elements in the array: "))
A = []
i = 1
while i <= N:
    A.append(i)
    i += 1

print(f"Array: {A}")
X = int(input("Enter number: "))
result = A.count(X)
print(f"Number of repetition: {result}")



