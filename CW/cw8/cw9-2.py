# Вивести список кольору, який найчастіше зустрічається в даному списку  
# [red, green, black, red, brown, red, blue, red, red, yellow ] використовуючи функцію filter.

colors =  ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
biggest_color = filter(lambda x: x == "red", colors )
print(list(biggest_color))