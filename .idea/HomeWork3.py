m = int(input("Введите размер массива: "))
my_array = []

for i in range(m):
    num = int(input("Введите число: "))
    my_array.append(num)
print("Массив:", my_array)

def even_odd(my_array1):
    ot=sum(my_array1[1::2])/sum(my_array1[0::2])
    return ot

print(even_odd(my_array))