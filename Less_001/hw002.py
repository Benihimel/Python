"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""

try:
    s = int(input("Enter the number of cranes: "))
    if s % 2 == 0:
        sKate = int(s / 6 * 4)
        sPete = int(s / 6)
        sSerezha = sPete
        print(f"Kate: {sKate}, Pete: {sPete}, Serezha: {sSerezha}")
    elif s % 2 != 0:
        print("The number cranes incorrect")
except ValueError:
    print("Abrakadabra")