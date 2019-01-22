# 1.  Створити список цілих чисел, які вводяться з терміналу 
# та визначити серед них максимальне та мінімальне число.

new_list = [int(input("enter number")) for x in range(int(input("enter amount numbers")))]
print("Max number is {}, min number is {}" .format(max(new_list), min(new_list)))