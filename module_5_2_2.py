class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= self.number_of_floors and new_floor != 0:
            print('-----------------------------------------------')
            print(f'В {self.name} {self.number_of_floors} этажей. Мы едем на {self.new_floor} этаж')
            for i in range(new_floor):
                print(i + 1)
        else:
            print('-----------------------------------------------')
            print(f'В ЖК {self.name} такого этажа не существует')

    # ---------------БЛОК С ПЕРЕГРУЗКОЙ---------------------

    def __eq__(self, other):
        print("__eq__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        print("__lt__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        print("__gt__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        print("__le__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        print("__ge__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        print("__ne__")
        if not isinstance(other, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        print("__add__")
        if not isinstance(value, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        self.number_of_floors += value
        return self


    def __radd__(self, value):
        print("__radd__")
        if not isinstance(value, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        print("__iadd__")
        if not isinstance(value, (int, House)):
            print('Правый операнд должен быть типом int или объектом House')
        self.number_of_floors += value
        return self



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Красный октябрь', 25)

# Лифт
h1.go_to(5)
h2.go_to(10)
h3.go_to(7)

# __str__
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
print('++++++++++++++++++++++++++++++++++++++++++++++++')

print('------------------------------------------')
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h3.name, h3.number_of_floors)

print('---------------------ПЕРЕГРУЗКА---------------------')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__