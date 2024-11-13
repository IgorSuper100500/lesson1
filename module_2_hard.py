import random


def first_field():
    numder = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_number = random.choice(numder)
    return first_number


number_1 = int(first_field())
print('Выпало в первом поле ', number_1)
list_ = []
str_ = ''
for i in range(1, number_1):
    for j in range(i+1, number_1):

        if number_1 % (i + j) == 0:
            list_.append([i,j])
            str_+= str(i) + str(j)
print ('Пары чисел :', *list_)
print('Число которое нужно подставить во второе поле : ', int(str_))
