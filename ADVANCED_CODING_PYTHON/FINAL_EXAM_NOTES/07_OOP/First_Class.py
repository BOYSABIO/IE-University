class Card:
    def __init__(self, id, amount = 0): #Initialize
        self.id = id #Attributes
        self.balance = amount
        return
    
    def show_balance(self): #Methods
        print("The balance is:", self.balance, "$")
        return
    
t1 = Card("7897879879", 1000) #Contructor
t1.show_balance()

