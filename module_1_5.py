# Задайте переменные разных типов данных:
immutable_var = 5, 4, 3, 2, 1, 'string'
print(immutable_var)
print(type(immutable_var))

# Изменение значений переменных:
# Выдаст ошибку  "unexpected indent" потому как нельзя изменять элементы кортежа
# immutable_var[0] = 10
# print(immutable_var)

# Создание изменяемых структур данных:
mutable_list = [1, 2, 3, 4, 5, 'string', True]
print(mutable_list)
print(type(mutable_list))
# Измените элементы списка mutable_list
mutable_list[3]= 15
print(mutable_list)
