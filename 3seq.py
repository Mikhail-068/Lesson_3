lst1 = input('Введите элементы 1-го списка: \n').split(',')
lst2 = input('Введите элементы 2-го списка: \n').split(',')

st1 = set(map(int, lst1))
st2 = set(map(int, lst2))

res = st1 ^ st2

print(*res)

