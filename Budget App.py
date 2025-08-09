class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = list({})

    def catt(self):
        return str(self.category)

    def __str__(self):
        affichage = ''
        for i in self.get_balance():
            affichage += i
            affichage += '\n'
        return affichage

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        affiche = []
        radius = (30 - len(self.category)) // 2
        title = ""
        for i in range(radius):
            title += '*'
        title += self.category
        for i in range(30 - (radius + len(self.category))):
            title += '*'
        affiche.append(title)
        somme = 0
        for dic in self.ledger:
            titre = ''
            dic['amount'] = float("{:.2f}".format(float(dic['amount'])))
            if dic['description'] != '':
                if dic['description'] == 'deposit':
                    dic['description'] = 'initial deposit'
                if len(dic['description']) <= 23:
                    titre += dic['description']
                    if len(str(dic['amount']).split('.')[-1]) == 2:
                        for i in range(30 - len(dic['description']) - len(str(dic['amount']))):
                            titre += ' '
                    else:

                        for i in range(29 - len(dic['description']) - len(str(dic['amount']))):
                            titre += ' '
                else:
                    for i in range(23):
                        titre += dic['description'][i]
                    titre += ' '
            else:
                for i in range(29 - len(str(dic['amount']))):
                    titre += ' '
            titre += str("{:.2f}".format(float(dic['amount'])))
            affiche.append(titre)
            somme += dic['amount']
        somme = 'Total: ' + str("{:.2f}".format(float(somme)))
        affiche.append(somme)
        return affiche

    def transfer(self, amount, categ):
        if self.check_funds(amount):
            to_transfer = 'Transfer to ' + categ.catt()
            self.ledger.append({'amount': -amount, 'description': to_transfer})
            from_transfer = 'Transfer from ' + self.category
            categ.deposit(amount, from_transfer)
            return True
        else:
            return False

    def check_funds(self, amount):
        money = 0
        for dic in self.ledger:
            money += dic['amount']
        if amount <= money:
            return True
        else:
            return False


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(14.54,'meklaaa ;n cheraaa')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
print(food)
