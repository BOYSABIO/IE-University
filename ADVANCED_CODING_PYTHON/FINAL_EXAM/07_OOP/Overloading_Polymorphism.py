class Card:
    def __init__(self, id, amount = 0):
        self.id = id
        self.balance = amount
        return
    
    def show_balance(self):
        print("The balance is {:.2f}$".format(self.balance))
        return
    
    def pay(self, amount):
        self.balance -= amount
        return
    

class Gold_Card(Card):
    def __init__(self, id, discount, amount = 0):
        self.id = id
        self.discount = discount
        self.balance = amount
        return
    
    def pay(self, amount):
        self.balance -= amount * (1 - self.discount / 100) #This is overloading (Takes initial information and adds)


card_1 = Card("111111", 1000)
card_2 = Gold_Card("222222", 1, 1000)

card_1.pay(100)
card_1.show_balance()
print()

card_2.pay(100)
card_2.show_balance()
print()