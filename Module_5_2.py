class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor <= self.number_of_floors and new_floor!=0:
            print('-----------------------------------------------')
            print(f'В {self.name} {self.number_of_floors} этажей. Мы едем на {self.new_floor} этаж')
            for i in range(new_floor):
                print(i + 1)
        else:
            print('-----------------------------------------------')
            print(f'В ЖК {self.name} такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Красный октябрь', 25)

# Лифт
h1.go_to(5)
h2.go_to(10)
h3.go_to(7)

print('------------------------------------------')
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print(h3.name, h3.number_of_floors)
