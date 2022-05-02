numbers = input().split()
numbers_2 = list(map(int, numbers))
print('Имеем числовую последовательность', numbers_2)
try:
    num = int(input("Введите число: "))
    print("Все верно. Число:", num)
except ValueError:
    print("Это не число.")

numbers_2.append(num)
count = 0
for i in range(1, len(numbers_2)):
    x = numbers_2[i]
    idx = i
    while idx > 0 and numbers_2[idx-1] > x:
        numbers_2[idx] = numbers_2[idx-1]
        idx -= 1
        count += 1
    numbers_2[idx] = x
def find(numbers_2, num):
    for i, a in enumerate(numbers_2):
        if a == num:
            return i
    return False
print(find(numbers_2, num))

def merge_sort(numbers_2):  # "разделяй"
    if len(numbers_2) < 2:  # если кусок массива равен 2,
        return numbers_2[:]  # выходим из рекурсии
    else:
        middle = len(numbers_2) // 2  # ищем середину
        left = merge_sort(numbers_2[:middle])  # рекурсивно делим левую часть
        right = merge_sort(numbers_2[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы
                 # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
                # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
for i in range(1, len(numbers_2)):
    x = numbers_2[i]
    idx = i
    while idx > 0 and numbers_2[idx-1] > x:
        numbers_2[idx] = numbers_2[idx-1]
        idx -= 1
    numbers_2[idx] = x
print('Объединёная числовая последовательность', numbers_2)

def binary_search(numbers_2, num, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if numbers_2[middle + 1] == num:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif num < numbers_2[middle + 1]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(numbers_2, num, left, middle - 1)
    else:  # иначе в правой
        return binary_search(numbers_2, num, middle + 1, right)
b = numbers_2.index(num)
b_ = binary_search(numbers_2, num, 0, len(numbers_2))
print('Счетчик итераций', count)
print('ID=', b)
if b_ > 0:
    print('ID элемента менее введенного', binary_search(numbers_2, num, 0, len(numbers_2)))

else:
    print('Элементы перед введенным числом отсутствуют')



