# 2.  Роздрукувати всі непарні числа менші 100.
# (написати два варіанти коду: один використовуючи
# оператор continue, а інший без цього оператора).

for i in range(1,100,2):
    print (i)
lse:
    print("The end")


for i in range(1,100,1):
    if i % 2 == 0:
        continue
    print(i)
else:
    print("The end")


j = 1
while j < 100:
    print(j)
    j += 2
else:
    print("The end")