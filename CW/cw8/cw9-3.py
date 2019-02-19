# Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], 
# перетворити цей список  в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

str_list = ['1','2','3','4','5','7']
int_list =[]
for item in str_list:
    int_list.append(int(item))

print(int_list)

str_list = ['1','2','3','4','5','7']

int_list = list(map(int, str_list))
print(int_list) 