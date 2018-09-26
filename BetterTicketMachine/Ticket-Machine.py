class TicketMachine:

    def __init__(self,cost):
        self.cost = cost
        self.total = 0
        self.balance = 0

    
    def getPrice(self):
        return self.cost

    def getBalance(self):
        return self.balance

    def insertMoney(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Use a positive amount rather than: " + amount)
            
    
    def printTicket(self):
        if self.balance >= self.cost:
            print("#"*10)
            print("The ticket line")
            print("Ticket price:")
            print("{price} cents.".format(price=self.cost))
            print("#"*10)
        
            self.balance -= self.cost
            self.total += self.cost
        else:
            print("You must insert at least: {money} more cents in order to buy a ticket.".format(money = self.cost - self.balance))
    
    def refundBalance(self):
        self.amountToRefund = self.balance
        self.balance = 0
        return self.amountToRefund