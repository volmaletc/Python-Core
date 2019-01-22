# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

list1 = [x for x in range(1,11,1) if x % 2 == 0]
print("Even numbers {}".format(list1))
list2 = [x for x in range(1,11,1) if x % 3 == 0 and x % 2 != 0]
print("Odd number which desn't divide into 2 {}".format(list2))
list3 = [x for x in range(1,11,1) if x%2!=0 and x%3!=0 ]
print("Number whit doesn't divide into 2 and 3 {}".format(list3))