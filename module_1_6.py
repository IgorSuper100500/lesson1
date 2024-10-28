#Работа со словарями:

# Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {'Igor' : 1986, 'Diana' : 1987, 'Mark' : 2022}
print(my_dict)
print(type(my_dict))

# Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict['Mark'])
print(my_dict.get('Aiza' , 'Такого имени нет в словаре'))

# Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Aiza':2023 ,
                'Bler': 2008})
print(my_dict)

# Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
age = my_dict.pop('Aiza')
print(age)
print(my_dict)

#Работа с множествами:

# Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 12, 4, 6, 1, 1, 2, 6, 12, 7, 4}
print(my_set)
print(type(my_set))

# Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(13)
my_set.add(17)
print(my_set)

# Удалите один любой элемент из множества my_set.
my_set.discard(12)
print(my_set)

