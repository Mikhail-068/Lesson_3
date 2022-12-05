count = int(input('Введите количество элементов: '))
lst = []

for i in range(count):
    arg = int(input(f'Введите {i+1} элемент: '))
    lst.append(arg)

lst.sort()

print("Вывод:", lst)