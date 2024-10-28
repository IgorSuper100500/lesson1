numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 11, 12, 13, 14, 15]

# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

primes = []
not_primes = []
for i in numbers:

    for j in range(2, i):
        if i % j == 0 or i == 1:
            not_primes.append(i)
            break
    else:
        if i != 1:
            primes.append(i)

print('Простые числа: ', primes)
print('Непростые числа: ', not_primes)
