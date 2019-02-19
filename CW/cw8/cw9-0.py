# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і 
# видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())


from random import randint

random_num = randint(0,100)

user_num = 0

while user_num != random_num:
    user_num = int(input("enter number"))
    if user_num > random_num:
        print("your number biggest than my")
    elif user_num < random_num:
        print("your number less than my")

print("congratulations you guess")