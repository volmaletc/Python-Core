# Спробуйте переписати наступний код через map. 
# Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.


names = ['Sam', 'Don', 'Daniel'] 

secret_names = map(hash, names)
print(list(secret_names)) 