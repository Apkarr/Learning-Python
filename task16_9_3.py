class Electro_wallet:
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance
el_wallet = Electro_wallet(customer='Клиент "Иван Петров"', balance="Баланс: 50 рублей")
print(el_wallet.customer, el_wallet.balance)


# Второй вариант решения 16.9.3, как недостаток, нельзя писать имя, фамилию клиента раздельно.
def customer_dp(**balance):
    for name, balance1 in balance.items():
        print("Клиент-", name, "баланс:", balance1, 'рублей')
customer_dp(Иван_Петров=50, Алексей_Иванов=60)
