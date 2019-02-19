# Напишіть скрипт, який обчислює площу прямокутника a*b, 
# площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі).


from math import pow, pi

def rectangle():
    a_rectangle = 5
    b_rectangle = 7
    sq_rectangle = a_rectangle * b_rectangle
    print(round((sq_rectangle), 3))

def triangle():
    a_triangle = 5
    h_triangle = 7
    sq_triangle = 0.5 * a_triangle * h_triangle
    print(round((sq_triangle), 3))

def cicle():
    r_cicle = 5
    sq_cicle = pi * pow(r_cicle, 2)
    print(round((sq_cicle), 3))


rectangle()
triangle()
cicle()