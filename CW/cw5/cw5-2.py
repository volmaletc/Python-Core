#Написати функцію, яка обчислює суму цифр введеного числа.

def sumd(n):
    sum = 0
    while n!=0:
        sum += n %10
        n = n // 10
    return sum    

k = int(input("enter number"))
g = sumd(k)
print(sumd(k))
