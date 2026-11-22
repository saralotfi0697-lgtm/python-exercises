class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self._balance=balance
    def __str__(self):
        return (f'{self.owner}:{self.balance}')
    def deposit(self,amount):
        if amount<=0:
            raise ValueError('amount should be positive!')
        self._balance+=amount
    def withdraw(self,amount):
        if amount<=0 :
            raise ValueError('amount should be positive!')
        if amount>self.balance:
            raise ValueError('balance is not enough!')
        self._balance-=amount
    @property
    def balance(self):
        return self._balance
b=BankAccount('Sara',10000)
b.deposit(10000)
b.withdraw(5000)
print(b.balance)
print(b)
        