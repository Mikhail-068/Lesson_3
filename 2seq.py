separator = input('Выберете разделитель: , ; / (но только один!) \n ')

if len(separator) > 1:
    print("выберите одно значение!")
    separator = input('Выберете разделитель: , ; / (но только один!) \n ')

s = [',', '/', ';']
while separator not in s:
    separator = input('Выберите разделитель из предложеныых  , ; / \n')

try:
    user = input('Вводите элементы через выбранный разделитель: ').split(separator)
    user = list(map(int, user))
    user = list(set(user))

    print('Результат: ', user)
except:
    print('Повнимательней!')