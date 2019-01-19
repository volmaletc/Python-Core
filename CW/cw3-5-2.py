#Вивести числа Фібоначі включно до введеного числа n, 
# використовуючи цикли. 
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
# ВВЕДЕНЕ ЧИСЛО = КІЛЬКОСТІ ЧИСЕЛ З ПОСЛІДОВНОСТІ

num = int(input("enter number: "))

fb0 = 0
fb = 1
i = 0
while i < num:
    if i < num:
        fb = fb + fb0
        print(fb)
    else:
        break
    i = i + 1
    if i < num:
        fb0 = fb + fb0
        print(fb0)
    else:
        break
    i = i + 1