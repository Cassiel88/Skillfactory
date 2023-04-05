per_cent = {'ТБК': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Пожалуйста, введите сумму депозита:'))
deposit = []
for key in per_cent: deposit.append(int(per_cent[key] * money / 100))
max_deposit = max(deposit)
print(deposit)
print('Максимальная сумма, которую Вы можете заработать - ' + str(max_deposit))

