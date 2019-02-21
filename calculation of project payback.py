
from tkinter import *
import tkinter.messagebox
import pprint
import matplotlib.pyplot as plt

win = Tk()
win.geometry('1200x800')

Investments = 0
Quantity_Of_Product = []
Cost_Per_Mounth = []
Price_Per_Mounth = []
Office_Rent = 0
Rent_Workshop = 0
SEO_Selary = 0
Accounter_salary = 0
Employee_salary= 0
Office_Rent_List = []
Rent_Workshop_List = []
SEO_Selary_List = []
Accounter_salary_List = []
Employee_salary_List = []
proffit_and_loss = []


# функція для запису даних в список з поля вводу кількості продукції
def save_quantity():
    for i in quantity_of_product:
        try:
            quantity_get = i.get()
            Quantity_Of_Product.append(float(quantity_get))
        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Please enter number in {} Quantity line'.format(i))
#           del Quantity_Of_Product[1:12]
    print(Quantity_Of_Product)

# функція для запису даних в список з поля вводу собівартості продукції
def save_cost():
    for ii in cost_of_product:
        try:
            cost_get = ii.get()
            Cost_Per_Mounth.append(float(cost_get))
        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Please enter number in {} Quantity line'.format(ii))
    print(Cost_Per_Mounth)

# функція для запису даних в список з поля вводу ціни за одиницю продукції
def save_price():
    for iii in price_per_product:
        try:
            price_get = iii.get()
            Price_Per_Mounth.append(float(price_get))
        except ValueError:
            tkinter.messagebox.showinfo('Error', 'Please enter number in {} Quantity line'.format(iii))
    print(Price_Per_Mounth)

# функція для запису даних в список з поля вводу щомісячних витрат
def save_monthly_expenses():
    i = 12
    Office_Rent = ofice_rent.get()
    Rent_Workshop = rent_workshop.get()
    SEO_Selary = seo_salary.get()
    Accounter_salary = acc_saalary.get()
    Employee_salary = employee_salary.get()
    Investments = investments.get()
    while i > 0:

        Office_Rent_List.append(float(Office_Rent))
        Rent_Workshop_List.append(float(Rent_Workshop))
        SEO_Selary_List.append(float(SEO_Selary))
        Accounter_salary_List.append(float(Accounter_salary))
        Employee_salary_List.append(float(Employee_salary))
        i -= 1
    print(Office_Rent_List)  
    print(Rent_Workshop_List)
    print(SEO_Selary_List)
    print(Accounter_salary_List)
    print(Employee_salary_List)
    print(Investments)


# функція для  обрахунку прибітків і збитків
def calculate_profit_and_loss():
    mounth = ['January','February','March','April','May',
    'June', "July", "August", "September", "October",
    "November", "December" ]
    global proffit_and_loss
    proffit_and_loss = [Q_Of_P * P_Per_M - Q_Of_P * C_Per_M
    - O_R_List - R_W_List - S_S_List - A_s_List - E_s_List for 
    Q_Of_P , P_Per_M , Q_Of_P , C_Per_M,    O_R_List , R_W_List , S_S_List , A_s_List , E_s_List in 
    zip(Quantity_Of_Product , Price_Per_Mounth , Quantity_Of_Product , Cost_Per_Mounth,
    Office_Rent_List , Rent_Workshop_List , SEO_Selary_List , Accounter_salary_List , Employee_salary_List)]
    print(list(proffit_and_loss))
    proffit_and_loss_dict = dict(zip(mounth, proffit_and_loss))
    print(proffit_and_loss_dict)
    #pprint.pprint(proffit_and_loss_dict, width=30)
    tkinter.messagebox.showinfo('Proffir and loss', 
    'Profit and loss in each month is {}'.format(proffit_and_loss_dict))


# функція для  обрахунку купності

def calculate_return_inv():
    total_pl = 0
    proffit_and_loss2 = [Q_Of_P * P_Per_M - Q_Of_P * C_Per_M
    - O_R_List - R_W_List - S_S_List - A_s_List - E_s_List for 
    Q_Of_P , P_Per_M , Q_Of_P , C_Per_M,    O_R_List , R_W_List , S_S_List , A_s_List , E_s_List in 
    zip(Quantity_Of_Product , Price_Per_Mounth , Quantity_Of_Product , Cost_Per_Mounth,
    Office_Rent_List , Rent_Workshop_List , SEO_Selary_List , Accounter_salary_List , Employee_salary_List)]
    for j in proffit_and_loss2:
        total_pl += j
    profitability = total_pl- float(investments.get())
    print(profitability)
    tkinter.messagebox.showinfo('Profitability', 'Profitability is {}'.format(profitability))
# функція для  побудови графіку доходів
def print_graph_inc():
    x = ['January','February','March','April','May',
    'June', "July", "August", "September", "October",
    "November", "December" ]
    y = proffit_and_loss
    print(proffit_and_loss)
    plt.plot(x, y)
    plt.show()
# функція для  для побудиви графіку доходів та витрат
def print_graph_inc_exp():
    x = ['January','February','March','April','May',
    'June', "July", "August", "September", "October",
    "November", "December" ]
    income1 = [Q_Of_P * P_Per_M for Q_Of_P , P_Per_M in zip(Quantity_Of_Product , Price_Per_Mounth)]
    expence1 =  [Q_Of_P * C_Per_M - O_R_List - R_W_List - S_S_List - A_s_List - E_s_List for 
    Q_Of_P , C_Per_M,    O_R_List , R_W_List , S_S_List , A_s_List , E_s_List in 
    zip(Quantity_Of_Product , Cost_Per_Mounth, Office_Rent_List ,
    Rent_Workshop_List , SEO_Selary_List , Accounter_salary_List , Employee_salary_List)]
    
    plt.plot(x, list(income1))
    plt.plot(x, list(expence1))
    plt.show()
# функція для  побудови графіку маржі
def print_graph_margin():
    income1 = [Q_Of_P * P_Per_M for Q_Of_P , P_Per_M in zip(Quantity_Of_Product , Price_Per_Mounth)]
    expence1 =  [Q_Of_P * C_Per_M - O_R_List - R_W_List - S_S_List - A_s_List - E_s_List for 
    Q_Of_P , C_Per_M,    O_R_List , R_W_List , S_S_List , A_s_List , E_s_List in 
    zip(Quantity_Of_Product , Cost_Per_Mounth, Office_Rent_List ,
    Rent_Workshop_List , SEO_Selary_List , Accounter_salary_List , Employee_salary_List)]
    margin = [in1 - ex1 for in1, ex1 in zip(income1, expence1)]
    x = ['January','February','March','April','May',
    'June', "July", "August", "September", "October",
    "November", "December" ]
    y2 = list(margin)
    plt.plot(x, y2)
    plt.show()



# Рядок місяців, аргумент вказує на якому рядку розміщені місяці 
def Mounth(m_row):
    mounth = ["Month", 'January','February','March','April','May',
    'June', "July", "August", "September", "October",
    "November", "December" ]
    m_column = 0
    for i in mounth:
        Label(text=i, relief=RIDGE,width=10).grid(row=m_row,column=m_column)
        m_column += 1

Mounth(5)
Mounth(9)
Mounth(13)

# поле для вводу інформації про кількість продукції
Label(text='Number of products releasedin the current month, quantity', 
relief=RIDGE,width=80).grid(row=4,column=3,columnspan=6)

quantity_of_product = []
q_column = 1
for i in range(12):
    quantity = Entry(win, width = 10)
    quantity.grid(row = 6, column = q_column) 
    quantity_of_product.append(quantity)
    q_column += 1

# поле для вводу інформації про витрати на одиницю продукції
Label(text='Cost of one issued product in the current month, UAH', 
relief=RIDGE,width=80).grid(row=8,column=3,columnspan=6)


cost_of_product = []
q_column = 1
for i in range(12):
    cost = Entry(win, width = 10)
    cost.grid(row = 10, column = q_column) 
    cost_of_product.append(cost)
    q_column += 1

# поле для вводу інформації про ціну заодиницю продукції
Label(text='Price of one unit in the current month, UAH', 
relief=RIDGE,width=80).grid(row=12,column=3,columnspan=6)

price_per_product = []
q_column = 1
for i in range(12):
    price = Entry(win, width = 10)
    price.grid(row = 14, column = q_column) 
    price_per_product.append(price)
    q_column += 1

# команди стирання даних якщо невірно заповнені поля
def del_quantity():
    del Quantity_Of_Product[:]
    print(Quantity_Of_Product)

def del_cost():
    del Cost_Per_Mounth[:]
    print(Cost_Per_Mounth)

def del_price():
    del Price_Per_Mounth[:]
    print(Price_Per_Mounth)


########### кнопки
# кнопка для запуску функції що записує дані про кількість в список
but = Button(win, text = "SAVE", command = save_quantity).grid(row = 7, column = 0)
# кнопка що стирає дані з списку в разі некоректного вводу
but = Button(win, text = "Clear", 
command = del_quantity).grid(row = 7, column = 1, columnspan=3)
# кнопка для запуску функції що записує дані про собівартість в список
but= Button(win, text = "SAVE", command = save_cost).grid(row = 11, column = 0)
# кнопка що стирає дані з списку в разі некоректного вводу
but = Button(win, text = "Clear", 
command = del_cost).grid(row = 11, column = 1, columnspan=3)
# кнопка для запуску функції що записує дані про ціну за одиницю в список
but = Button(win, text = "SAVE", command = save_price).grid(row = 15, column = 0)
# кнопка що стирає дані з списку в разі некоректного вводу
but = Button(win, text = "Clear", 
command = del_price).grid(row = 15, column = 1, columnspan=3)
# кнопка для запуску функції що записує дані про щомісячні витрати
but = Button(win, text = "SAVE", command = save_monthly_expenses).grid(row = 23, column = 1)
# звіт про прибутки і збитки
but = Button(win, text = "Profit and Loss Statement", 
command = calculate_profit_and_loss).grid(row = 25, column = 0, columnspan=3)
# окупність
but = Button(win, text = "Return on investment", 
command = calculate_return_inv).grid(row = 26, column = 0, columnspan=3)
# Графік прибутків
but = Button(win, text = "Income graph", 
command = print_graph_inc).grid(row = 27, column = 0, columnspan=3)
# графік доходів та витрат
but = Button(win, text = "Income and expense graph", 
command = print_graph_inc_exp).grid(row = 28, column = 0, columnspan=3)
# графік маржі
but = Button(win, text = "Margin graph", 
command = print_graph_margin).grid(row = 29, column = 0, columnspan=3)
# графік маржі
but = Button(win, text = "Margin graph", 
command = print_graph_margin).grid(row = 29, column = 0, columnspan=3)




########### одиночні поля
Label(text='Investments', relief=RIDGE,width=20).grid(row=2,column=0,columnspan=2)
investments = Entry(win, width = 10)
investments.grid(row = 2, column = 2) 

Label(text='Continuous costs, UAH', 
relief=RIDGE,width=80).grid(row=16,column=3,columnspan=6)

Label(text='Office Rent', relief=RIDGE,width=20).grid(row=18,column=0,columnspan=2)
ofice_rent = Entry(win, width = 10)
ofice_rent.grid(row = 18, column = 2) 

Label(text='Rent a workshop', relief=RIDGE,width=20).grid(row=19,column=0,columnspan=2)
rent_workshop = Entry(win, width = 10)
rent_workshop.grid(row = 19, column = 2)

Label(text='SEO salary', relief=RIDGE,width=20).grid(row=20,column=0,columnspan=2)
seo_salary = Entry(win, width = 10)
seo_salary.grid(row = 20, column = 2)

Label(text='Accountants salary', relief=RIDGE,width=20).grid(row=21,column=0,columnspan=2)
acc_saalary = Entry(win, width = 10)
acc_saalary.grid(row = 21, column = 2)

Label(text='Employee salary', relief=RIDGE,width=20).grid(row=22,column=0,columnspan=2)
Label(text='* Employee salary * quantity of employee', relief=RIDGE,width=40).grid(row=22,column=3, columnspan=4)
employee_salary = Entry(win, width = 10)
employee_salary.grid(row = 22, column = 2)



mainloop()