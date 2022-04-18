class volunteer_dp():
    def __init__(self, name, surname, siti, status):
        self.name = name
        self.surname = surname
        self.siti = siti
        self.status = status
Ivanov = volunteer_dp(name='Николай', surname='Иванов', siti='г. Москва', status='статус "Наставник"')
Karcev = volunteer_dp(name='Валентин', surname='Карцев', siti='г. Москва', status='статус "Наставник"')
Petrov = volunteer_dp(name='Иван', surname='Петров', siti='г. Москва', status='статус "Наставник"')
print(Petrov.name, Petrov.surname, Petrov.siti, Petrov.status)
print(Ivanov.name, Ivanov.surname, Ivanov.siti, Ivanov.status)
print(Karcev.name, Karcev.surname, Karcev.siti, Karcev.status)




