# Знайти найбільший елемент в списку  використовуючи функцію reduce

# from functools import reduce
# num_list = [0, 1, 2, 3, 4, 5, 6, 7]
# max_number = reduce(lambda x, y: max(x ,y), num_list)
# print(max_number)

from functools import reduce

items = [1, 24, 88, 55, 47]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)