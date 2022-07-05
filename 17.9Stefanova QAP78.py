a = [int(i) for i in (input('введите числа через пробел').split())] #создаем список чисел из вводимой через пробел последовательности
b = int(input('введите число')) 

def binary_search(array, b, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует


    middle = (right + left) // 2  # находим середину
    if array[middle] == b:  # если элемент в середине,
        return middle  # возвращаем этот индекс

    elif b < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, b, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, b, middle + 1, right)


if b < min(a) or b > max(a):
    print('введеное число не коректно')
else:
    a.append(b)
    array = sorted(a)
    minimum = array[0]
    maximum = array[-1]
    print(binary_search(array, b, 0, maximum - 1))
    





