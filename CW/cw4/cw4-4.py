# Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login = input("Enter your login please: ")
while login != "First":
    print("{} incorrect login, try again".format(login))
    login = input("Enter your login please: ")
else:
    print("Hello {}".format(login))
