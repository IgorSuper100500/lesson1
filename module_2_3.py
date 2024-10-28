my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор,
# пока не встретите отрицательное или не закончится список (выход за границу).

index = 0
end = len(my_list)
while index < end:

    if my_list[index] > 0:
        print(my_list[index])
    elif my_list[index] < 0:
        break
    index += 1