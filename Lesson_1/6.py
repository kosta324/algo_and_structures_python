# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
symbol = chr(int(input(f'Введите номер буквы в алфавите:\n')) + ord('a') - 1)
print(f'Ваша буква: {symbol}')
