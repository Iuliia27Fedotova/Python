def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        print('Число отсутствует в последовательности')
    middle = (right + left) // 2
    if array[middle] < element <= array[middle+1]:
        print('Индекс числа, меньше введенного, а следующий за ним больше или равен этому числу = ', middle)
    elif element <= array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle+1, right)


string = input('Введите последовательность чисел через пробел: ')
try:
    spisok = list(map(int, string.split()))
    number = int(input('Введите любое число: '))
except ValueError:
    print('Ошибка ввода данных')
else:
    spisok.append(number)
    qsort(spisok, 0, len(spisok)-1)
    print('Отсортированная последовательность c добавленным в неё введенным числом: ', spisok)
    if number == spisok[0]:
        print('Введеное число минимальное в последовательности')
    elif number == spisok[len(spisok)-1] and number != spisok[len(spisok)-2]:
        print('Введеное число максимальное в последовательности. Индекс числа, меньше введеного = ', len(spisok)-2)
    else:
        index_number = binary_search(spisok, number, 0, len(spisok)-1)
