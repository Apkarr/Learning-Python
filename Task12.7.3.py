money = int(input())
p1: int = int(money / 100)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent = list(per_cent.values())
deposit = []
i = per_cent
for i in per_cent:
    s = i * p1
    deposit.append(int(s))
print(deposit)
print(max(deposit))





