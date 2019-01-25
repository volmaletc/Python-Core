# 1.  Написати програму, яка обчислює площу прямокутника, трикутника 
# та кола (написати три функції для обчислення площі,
# і викликати їх в головній програмі в залежності від вибору користувача)

def sq_rectangle(a, b):
    sq = a * b
    print(sq)

def sq_triangle(a, b):
    sq = 1/2 * a * b
    print(sq)

def sq_circle(a):
    Pi = 3.14
    sq = Pi * a **2
    print(sq)

your_choice = int(input("please input your choice(1 - rectangle, 2 - triangle, 3 - circle): "))
if your_choice == 1:
    a = int(input("enter the first side of the rectangle: "))
    b = int(input("enter the second side of the rectangle: "))
    sq_rectangle(a, b)
elif your_choice == 2:
    a = int(input("enter the height of the triangle: "))
    b = int(input("enter the basis of the triangle: "))
    sq_triangle(a, b)
elif your_choice == 3:
    a = int(input("enter the radius of the circle: "))
    sq_circle(a)
else:
    print("wrong, input number 1, 2 or 3")
