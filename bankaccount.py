class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.transactions = []
    def deposit(self,amount):
        if amount<=0:
           raise ValueError('amount must be positive!')
        self.balance+=amount
        self.transactions.append(('deposit',amount))
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError('amount must be positive!')
        elif amount>self.balance:
            raise ValueError('Insufficient balance')
        self.balance-=amount
        self.transactions.append(('withdraw',amount))
    def show_info(self):
        return(f'Name of Owner:{self.owner}\nBalance:{self.balance}')
    def show_transactions(self):
        for kind , amount  in self.transactions:
          print(f'{kind}:{amount}')
    def transfer(self,other,amount):
        self.withdraw(amount)
        other.deposit(amount)

ob=BankAccount('Sara',10000)
ob2=BankAccount('mina',12000)
print(ob.show_info())
ob.deposit(10000)
ob.withdraw(800)
ob.show_transactions()
print(ob.balance)
ob.transfer(ob2,1200)
print(ob2.show_info())


try:
   ob.withdraw(50000)
   ob.transfer(ob2,19999999)
except ValueError as e:
    print(f'Error:{e}')

        