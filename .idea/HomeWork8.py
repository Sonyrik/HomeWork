import itertools

m = int(input("Введите размер первого массива: "))
my_array1 = []

for i in range(m):
    num = int(input("Введите число: "))
    my_array1.append(num)
print("Первый массив:", my_array1)

n = int(input("Введите размер второго массива: "))
my_array2 = []

for i in range(n):
    num = int(input("Введите число: "))
    my_array2.append(num)
print("Второй массив:", my_array2)


def cartesian_product(my_array1, my_array2):
    lists = [my_array1, my_array2]
    result = list(itertools.product(*lists))
    return result

print("Декартово произведение массивов:", cartesian_product(my_array1, my_array2))
print("Декартово произведение массивов:", cartesian_product([1,2],['A','B']))
