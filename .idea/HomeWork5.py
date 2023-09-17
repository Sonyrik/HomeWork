n = int(input("Введите размер массивов: "))
my_array1 = []

for i in range(n):
    num = input("Введите элемент первого массива: ")
    my_array1.append(num)
print("Первый массив:", my_array1)

my_array2 = []

for i in range(n):
    num = input("Введите элемент второго массива: ")
    my_array2.append(num)
print("Второй массив:", my_array2)


def corresponding_pairs(my_array1, my_array2):
    my_array3 = []
    for i in range(n):
        num = (my_array1[i],my_array2[i])
        my_array3.append(num)
    return my_array3



print("Третий массив:", corresponding_pairs(my_array1, my_array2))
print("Третий массив:", corresponding_pairs([1,2],['A','B']))