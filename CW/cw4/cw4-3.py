# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)

fact_number = int(input("Enter number: "))
f = 1
if f == 0:
    print("Factorial fom {} is 1".format(fact_number))
else:
    for i in range(1, (fact_number + 1)):
        f*= i
    print("Factorial from {} is {}".format(fact_number, f))

fact_number = int(input("Enter number: "))
f = 1
if f == 0:
    print("Factorial fom {} is 1".format(fact_number))
else:
    while fact_number > 1:
        f = f * fact_number
        fact_number = fact_number - 1
    print("Factorial from {} is {}".format(fact_number, f))