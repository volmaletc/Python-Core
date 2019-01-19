#Вивести числа Фібоначі включно до введеного числа n, 
# використовуючи цикли. 
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
# ЧИСЛО З ПОСЛІДОВНОСТІ Є МЕНШИМ А НІЖ ВВЕДЕНЕ

num = int(input("enter number: "))

fb0 = 0
fb = 1
i = 0
while fb0 < num:
    fb = fb + fb0
    if fb < num:
        print(fb)
    else:
         break
    fb0 = fb + fb0
    if fb0 < num:
        print(fb0)
    else:
        break
