class Card:
    def __init__(self, id, amount = 0): #Initialize
        self.id = id #Attributes
        self.balance = amount
        return
    
    def show_balance(self): #Methods
        print("The balance is:", self.balance, "$")
        return
    

class discount_card(Card):
    def __init__(self, id, discount, amount = 0):
        self.id = id
        self.discount = discount
        self.balance = amount
        return
    
    def show_discount(self): #Exclusive method of class discount_card
        print("Discount of", self.discount, "% of payments.")
        return
    
t = discount_card("12341234", 2, 1000)

t.show_balance()
print()
t.show_discount()