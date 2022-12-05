user = input('Введите элементы списка через запятую: ').split(',')
user = list(map(int, user))
user = list(set(user))

print('Результат: ', user)