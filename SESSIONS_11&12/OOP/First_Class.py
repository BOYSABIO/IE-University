class Card:
    def __init__(self, id, amount): #Initialize
        self.id = id #Attributes
        self.amout = amount
        return
    
    def show_balance(self): #Methods
        print("The balance is:", self.balance, "$")
        return
    
t1 = Card("7897879879") #Contructor
t1.show_balance()
