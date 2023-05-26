"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

try:
    var = int(input("Enter number: "))
    if 100 < var < 1000:
        var1 = int(var % 10)
        var2 = int(var % 100 // 10)
        var3 = int(var / 10 // 10)
        print(f'Sum digit {var3} + {var2} + {var1} -> {var1 + var2 + var3}')
    elif 100 > var or var > 999:
        print("The input isn't correct.")
except ValueError:
    print("Abrakadabra")





